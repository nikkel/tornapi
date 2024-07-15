# Changelog

## Version 0.2.0 - Torn Endpoint Release

### Torn Endpoint
- Added the `TornEndpoint` class to handle torn-related API calls.
  - Implemented methods for each torn selection endpoint
    - `bank`
    - `cards`
    - `chainreport`
    - `cityshops`
    - `companies`
    - `competition`
    - `dirtybombs`
    - `education`
    - `factiontree`
    - `getCards`
    - `getDirtyBombs`
    - `gyms`
    - `honors`
    - `itemdetails`
    - `items`
    - `itemstats`
    - `logcategories`
    - `logtypes`
    - `medals`
    - `organisedcrimes`
    - `pawnshop`
    - `pokertables`
    - `properties`
    - `rackets`
    - `raidreport`
    - `raids`
    - `rankedwarreport`
    - `rankedwars`
    - `rockpaperscissors`
    - `searchforcash`
    - `shoplifting`
    - `stats`
    - `stocks`
    - `territory`
    - `territorynames`
    - `territorywarreport`
    - `territorywars`
    - `timestamp`

### Added
  - The territory method can now accept a single string or a list of strings representing territories.
  - The chainreport method can now accept a parameter to specify the chain ID.
  - The companies method can now accept an optional parameter to specify the company ID.
  - The education method can now accept an optional parameter to specify the education ID.
  - The gyms method can now accept an optional parameter to specify the gym ID.
  - The honors method can now accept an optional parameter to specify the honor ID.
  - The itemdetails method can now accept a parameter to specify the unique item ID.
  - The items method can now accept an optional parameter to specify the item ID.
  - The medals method can now accept an optional parameter to specify the medal ID.
  - The organisedcrimes method can now accept an optional parameter to specify the organized crime ID.
  - The properties method can now accept an optional parameter to specify the property ID.
  - The raidreport method can now accept a parameter to specify the raid ID.
  - The rankedwarreport method can now accept a parameter to specify the ranked war ID.
  - The stocks method can now accept an optional parameter to specify the stock ID.

### Fixes
- Updated the url in setup.py to the repo link

## Version 0.1.0 - Initial Release

### Initial Setup
- Created the initial structure of the `tornapi` library.
  - Organized the project with directories and files for `client`, `endpoints`, `exceptions`, and `tests`.
  - Added `setup.py`, `requirements.txt`, `LICENSE`, `CHANGELOG.md`, and `README.md` for package distribution and documentation.

### API Client
- Implemented the `TornAPI` class.
  - Enabled setting the API key during the initialization of the `TornAPI` client.
  - Added a rate limiter to restrict the number of requests to 100 per minute by default.
  - Allowed users to set a custom rate limit during initialization.
  - Ensured thread safety in the rate-limiting mechanism using a lock.
  - Implemented a method to make requests to the Torn API with error handling.

### Exception Handling
- Created custom exceptions for handling API errors.
  - Implemented `TornAPIError` to raise specific errors based on the API response status and content.

### User Endpoint
- Added the `UserEndpoint` class to handle user-related API calls.
  - Implemented methods for each user selection endpoint:
    - `ammo`
    - `attacks`
    - `attacksfull`
    - `bars`
    - `basic`
    - `battlestats`
    - `bazaar`
    - `cooldowns`
    - `crimes`
    - `discord`
    - `display`
    - `education`
    - `equipment`
    - `events`
    - `gym`
    - `hof`
    - `honors`
    - `icons`
    - `inventory`
    - `jobpoints`
    - `log`
    - `lookup`
    - `medals`
    - `merits`
    - `messages`
    - `missions`
    - `money`
    - `networth`
    - `newevents`
    - `newmessages`
    - `notifications`
    - `perks`
    - `personalstats`
    - `profile`
    - `properties`
    - `refills`
    - `reports`
    - `revives`
    - `revivesfull`
    - `skills`
    - `stocks`
    - `timestamp`
    - `travel`
    - `weaponexp`
    - `workstats`
  - Allowed methods to accept an optional `user_id` parameter to fetch data for other users.

### Deprecation Handling
- Added a decorator for marking functions and classes as deprecated, which emits a warning when used.
