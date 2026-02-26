# This module lets us use flask using slugs instead of file references

# Valid slugs

valid_slugs = {
    "index": "index.html",
    "about": "about.html",
    "contact": "contact.html",
    "components": "components.html",
    "thankyou": "thankyou.html",
    "work": "work.html",
    "works": "works.html",
    "404": "404.html",
    }

def check_slug(slug) -> bool:
    if slug in valid_slugs:
        return True
    else:
        return False

def return_file(slug) -> str:
    if not(check_slug(slug)): return None # Slug isn't valid

    return valid_slugs[slug]