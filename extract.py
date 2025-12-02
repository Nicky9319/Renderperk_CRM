import requests
import json
import os
import re
from urllib.parse import urlparse

# Hardcoded list of Reddit post URLs
REDDIT_POST_URLS = [
    "https://www.reddit.com/r/graphic_design/comments/14zln3r/how_much_does_it_cost_on_a_render_farm_to_make_a/",
    "https://www.reddit.com/r/Maya/comments/15r6cg9/render_farm/",
    "https://www.reddit.com/r/AfterEffects/comments/1csl0jr/are_render_farms_worth_it/",
    "https://www.reddit.com/r/blender/comments/qvy2l7/anyone_here_with_experience_with_renderstreets/",
    "https://www.reddit.com/r/vfx/comments/1is7d7o/company_wants_to_create_a_rendering_farm/",
    "http://reddit.com/r/blender/comments/npf4fi/looking_to_rent_out_my_small_render_farm_for_real/",
    "https://www.reddit.com/r/blender/comments/17q2dbh/should_i_opt_for_rendering_using_a_render_farm_or/",
    "https://www.reddit.com/r/Houdini/comments/1afjqp7/render_farms/",
    "https://www.reddit.com/r/MotionDesign/comments/16ltgef/how_to_quote_for_3d_rendering_farm_cost/",
    "https://www.reddit.com/r/blender/comments/q9yiwd/render_farm_that_doesnt_cost_several_thousand/",
    "https://www.reddit.com/r/blender/comments/10vur0m/this_one_took_nine_days_to_render_why_do_i_do/",
    "https://www.reddit.com/r/blender/comments/qlea03/does_anyone_here_know_a_cheap_render_farm_for/",
    "https://www.reddit.com/r/vfx/comments/14nks45/what_are_peoples_favorite_online_renderfarms/",
    "https://www.reddit.com/r/vfx/comments/kdj9f1/fox_renderfarm_irenderfarm_which_one_is_better/",
    "https://www.reddit.com/r/Maya/comments/17izswq/render_farm/",
    "https://www.reddit.com/r/blender/comments/18odbvr/what_render_farm_could_you_recommend_for/",
    "https://www.reddit.com/r/blender/comments/1hv1wq8/how_does_a_render_farm_work/",
    "https://www.reddit.com/r/sysadmin/comments/1m4lfod/render_farm_recommendations/",
    "https://www.reddit.com/r/blender/comments/16fwdn0/what_are_the_best_online_render_farms/",
    "https://www.reddit.com/r/blender/comments/19bzon5/any_free_renderfarms/",
    "https://www.reddit.com/r/blenderhelp/comments/193hrtn/rendering_farm_recommendations/"
]

def extract_post_id_and_title(url):
    """
    Extract post ID and title from Reddit URL.
    URL format: https://www.reddit.com/r/subreddit/comments/POST_ID/TITLE/
    Returns: (post_id, title) tuple
    """
    # Parse the URL
    parsed = urlparse(url)
    path = parsed.path
    
    # Match the pattern: /r/subreddit/comments/POST_ID/TITLE/
    pattern = r'/r/[^/]+/comments/([^/]+)/([^/]+)/?'
    match = re.search(pattern, path)
    
    if match:
        post_id = match.group(1)
        title = match.group(2)
        return post_id, title
    else:
        # Fallback: try to extract from path segments
        parts = [p for p in path.split('/') if p]
        if 'comments' in parts:
            idx = parts.index('comments')
            if idx + 2 < len(parts):
                return parts[idx + 1], parts[idx + 2]
    
    # If we can't parse, use a sanitized version of the URL
    sanitized = re.sub(r'[^a-zA-Z0-9]', '_', url)
    return sanitized[:20], 'unknown'

def check_if_already_processed(url):
    """
    Check if the JSON file for this URL already exists in unprocessed or processed folder.
    Returns: (exists: bool, folder_name: str or None)
    """
    post_id, title = extract_post_id_and_title(url)
    filename = f"{post_id}_{title}.json"
    
    # Check in unprocessed folder
    unprocessed_path = os.path.join("unprocessed", filename)
    if os.path.exists(unprocessed_path):
        return True, "unprocessed"
    
    # Check in processed folder
    processed_path = os.path.join("processed", filename)
    if os.path.exists(processed_path):
        return True, "processed"
    
    return False, None

def fetch_and_save_reddit_post(url):
    """
    Fetch JSON data from Reddit post and save to unprocessed folder.
    Returns: (success: bool, error_message: str or None)
    """
    try:
        # Append .json to the URL
        json_url = url.rstrip('/') + '.json'
        
        # Make request to Reddit API
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(json_url, headers=headers, timeout=30)
        
        # Check if request was successful
        if response.status_code != 200:
            return False, f"HTTP {response.status_code}: {response.reason}"
        
        # Parse JSON response
        try:
            json_data = response.json()
        except json.JSONDecodeError as e:
            return False, f"Invalid JSON response: {str(e)}"
        
        # Extract post ID and title from URL
        post_id, title = extract_post_id_and_title(url)
        
        # Create filename: post_id_title.json
        filename = f"{post_id}_{title}.json"
        
        # Ensure unprocessed folder exists
        output_dir = "unprocessed"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save JSON to file
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        return True, None
        
    except requests.exceptions.RequestException as e:
        return False, f"Request error: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    """
    Main function to process all Reddit post URLs.
    """
    if not REDDIT_POST_URLS:
        print("No Reddit post URLs found in the list. Please add URLs to REDDIT_POST_URLS.")
        return
    
    print(f"Processing {len(REDDIT_POST_URLS)} Reddit post(s)...")
    print("-" * 60)
    
    failed_urls = []
    successful_count = 0
    skipped_count = 0
    
    # Process each URL sequentially
    for i, url in enumerate(REDDIT_POST_URLS, 1):
        print(f"[{i}/{len(REDDIT_POST_URLS)}] Processing: {url}")
        
        # Check if already processed
        already_exists, folder = check_if_already_processed(url)
        if already_exists:
            print(f"  ⊘ This URL has been processed (file exists in {folder}/ folder)")
            skipped_count += 1
            print()
            continue
        
        success, error = fetch_and_save_reddit_post(url)
        
        if success:
            post_id, title = extract_post_id_and_title(url)
            filename = f"{post_id}_{title}.json"
            print(f"  ✓ Successfully saved to: unprocessed/{filename}")
            successful_count += 1
        else:
            print(f"  ✗ Failed: {error}")
            failed_urls.append((url, error))
        
        print()
    
    # Display summary
    print("-" * 60)
    print(f"Processing complete!")
    print(f"  Successful: {successful_count}/{len(REDDIT_POST_URLS)}")
    print(f"  Skipped (already processed): {skipped_count}/{len(REDDIT_POST_URLS)}")
    print(f"  Failed: {len(failed_urls)}/{len(REDDIT_POST_URLS)}")
    
    # Display failed URLs if any
    if failed_urls:
        print("\nFailed URLs:")
        for url, error in failed_urls:
            print(f"  - {url}")
            print(f"    Error: {error}")

if __name__ == "__main__":
    main()

