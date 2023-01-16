import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")

# To change the env: $ export ENV_Name='production' and run main.py -> env changed to 'production'
# 1. checking substrings
# 2. pretty handy if you dont want to commit secrets/keys to source code
