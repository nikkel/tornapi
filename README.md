# TornAPI

TornAPI is a Python library for interacting with the Torn API. This library provides easy access to Torn's various API endpoints, including user, city, and faction endpoints. It supports rate limiting and allows users to set custom API keys.

- Easy-to-use API client.
- Rate limiting to avoid exceeding the API request limits.
- Custom exceptions for error handling.
- Comprehensive support for user selection endpoints.

## Features

- Access to multiple Torn API endpoints
- Rate limiting to prevent exceeding API request limits
- Customizable API key and rate limit settings
- Optional user ID parameter for user-related endpoints
- Exception handling for API errors
- Deprecation warnings for deprecated functions

## Installation

To install TornAPI, simply use pip:

```bash
pip install tornapi
```

## Usage

Here's an example of how to use the TornAPI library:

```python
from tornapi import TornAPI

# Initialize the API client
api = TornAPI('your-api-key', rate_limit=100)

# Fetch basic user data
user_data = api.user.basic()
print(user_data)

# Fetch user icons
icons_data = api.user.icons()
print(icons_data)

# Fetch another user's profile by user ID
profile_data = api.user.profile(user_id=123456)
print(profile_data)

# Fetch city data
city_data = api.city()
print(city_data)

# Fetch faction data
faction_data = api.faction.get_faction(1234)
print(faction_data)
```