import spacy
import re

# Load English language model
nlp = spacy.load("en_core_web_sm")

def analyze_error_with_nlp(error_text):
    # Define failure categories and their associated keywords, reasons, resolutions, and prevention plans
    failure_categories = {
        "3rd party error": {
            "keywords": ["3rd party"],
            "reason": "Error caused by third-party dependency.",
            "resolution": "Check compatibility with third-party dependencies. Update or replace as necessary.",
            "prevention": "Regularly update third-party dependencies and ensure compatibility with your system."
        },
        "Automated test failure": {
            "keywords": ["Automated test", "test job", "archives","http error 404"],
            "reason": "Automated test failure occurred.",
            "resolution": "Investigate failing test cases, debug issues, and make necessary code changes.",
            "prevention": "Better erroring message (either via Krishnabot or via Jenkins console) that our process doesn't allow version bumps without code change, maintain test suites, and ensure test environment consistency."
        },
        "code issue": {
            "keywords": ["code issue", "exception occurred during task","has an invalid value"],
            "reason": "Error caused by issues in the codebase.",
            "resolution": "Review and debug code, fix any syntax or logical errors.",
            "prevention": "Document DB cluster host details needs to be checked before executing, perform code reviews, and use static code analysis tools."
        },
        "detached head": {
            "keywords": ["detached head"],
            "reason": "Error due to detached head in version control.",
            "resolution": "Reattach the HEAD to a branch or commit changes to a branch.",
            "prevention": "Avoid detaching the HEAD unintentionally. Commit changes to branches regularly."
        },
        "disk space": {
            "keywords": ["disk space", "low disk space"],
            "reason": "Error caused by insufficient disk space.",
            "resolution": "Free up disk space by deleting unnecessary files or expanding storage capacity.",
            "prevention": "Regularly monitor disk space usage and clean up unnecessary files."
        },
        "existing version": {
            "keywords": ["existing version", "version dashboard", "wrong version", "version already exists", "stopping the build", "commit as only an update"],
            "reason": "Error due to conflicting or incorrect version.",
            "resolution": "Ensure the correct version is used or resolve version conflicts.",
            "prevention": "Maintain version consistency and verify versions before deployment."
        },
        "failed build": {
            "keywords": ["failed build", "failed to deploy instance"," commit's build result"],
            "reason": "Error occurred during the build process or deployment.",
            "resolution": "Investigate build or deployment failures, fix issues, and retry.",
            "prevention": "Maintain a stable build and deployment process, perform regular tests."
        },
        "Gradle concurrency error": {
            "keywords": ["Gradle concurrency"],
            "reason": "Error caused by concurrency issues in Gradle.",
            "resolution": "Review Gradle configuration, dependencies, and parallel execution settings.",
            "prevention": "Avoid complex dependency graphs, manage concurrency effectively."
        },
        "incorrect packer version": {
            "keywords": ["incorrect packer version"],
            "reason": "Error due to incorrect Packer version.",
            "resolution": "Install or update Packer to the correct version.",
            "prevention": "Ensure correct Packer version is used and manage versions carefully."
        },
        "jenkins error": {
            "keywords": ["jenkins error"],
            "reason": "Error occurred in Jenkins.",
            "resolution": "Investigate Jenkins logs, configuration, and dependencies.",
            "prevention": "Regularly monitor Jenkins, update plugins, and maintain system stability."
        },
        "jenkins plugin issue": {
            "keywords": ["jenkins plugin issue", "jenkinsci", "plugins", "end of pipelinek8s", "error when executing success post", "completed with status unstable"],
            "reason": "Error caused by issues with Jenkins plugins.",
            "resolution": "Review plugin configuration, update or replace problematic plugins.",
            "prevention": "Regularly update Jenkins plugins, test compatibility before deployment."
        },
        "low disk space issue in jenkins": {
            "keywords": ["low disk space in jenkins"],
            "reason": "Error due to low disk space in Jenkins environment.",
            "resolution": "Free up disk space, optimize Jenkins workspace usage.",
            "prevention": "Regularly monitor disk space in Jenkins, clean up old builds and artifacts."
        },
        "missing ansible variable": {
            "keywords": ["missing ansible variable"],
            "reason": "Error due to missing variable in Ansible playbook.",
            "resolution": "Define the missing variable or handle missing variable gracefully.",
            "prevention": "Ensure all required variables are defined in Ansible playbooks."
        },
        "failed to deploy instance":{
            "keywords":["unreachable"," authentication failed"],
            "reason": "Deployment process encounters issues preventing successful instance deployment.",
            "resolution": " Investigate logs, fix configuration errors, resolve dependencies, and retry deployment.",
            "prevention" : "Implement robust testing, update configurations, monitor resources, and provide training.",
        },
        "race condition": {
            "keywords": ["race condition", "concurrent access", "synchronization issue"],
            "reason": "Error caused by a race condition.",
            "resolution": "Analyze and synchronize concurrent access to shared resources.",
            "prevention": "Use proper synchronization mechanisms, avoid shared state where possible."
        },
        "script not available": {
            "keywords": ["script not available"],
            "reason": "Error occurred because the script is not available.",
            "resolution": "Ensure the script is present and accessible.",
            "prevention": "Maintain script availability and ensure proper permissions."
        },
        "user error": {
            "keywords": ["correct cluster", "search criteria", "remove ocr lock", "has an invalid value"],
            "reason": "Error caused by user action or input.",
            "resolution": "Provide clear instructions, and implement validation checks.",
            "prevention": "Provide user training, implement user-friendly interfaces, and validate input."
        },
        "missing failure category": {
            "keywords": ["missing failure category"],
            "reason": "Error category not specified.",
            "resolution": "Identify and categorize the error.",
            "prevention": "Ensure errors are properly categorized for effective analysis and resolution."
        },
        "incorrect sql query": {
            "keywords": ["SQL syntax","mysql server version", "table", "unknown column", "foreign key constraint", "incorrect number of arguments for procedure", "unknown column","duplicate entry"],
            "reason": "Error caused by incorrect SQL syntax.",
            "resolution": "Review and correct the SQL query syntax.",
            "prevention": "Adopt coding standards, use parameterized queries to avoid SQL injection."
        }
    }

    # Initialize variables for category and matching score
    matching_category = "missing failure category"
    max_score = 0

    # Iterate through failure categories and find best match based on keyword overlap
    for category, info in failure_categories.items():
        category_keywords = info["keywords"]
        pattern = '|'.join([re.escape(keyword) for keyword in category_keywords])
        matches = re.findall(pattern, error_text.lower())
        score = len(matches)
        if score > max_score:
            max_score = score
            matching_category = category
            print(category_keywords)
            

    # Return matching category along with reason, resolution, and prevention plan
    return matching_category, failure_categories[matching_category]["reason"], failure_categories[matching_category]["resolution"], failure_categories[matching_category]["prevention"]

# Take error text as input from the user
error_text = input("Enter the error text: ")

# Analyze error text using NLP
category, reason, resolution, prevention = analyze_error_with_nlp(error_text)
print("Failure Category:", category)
print("Reason:", reason)
print("Resolution:", resolution)
print("Prevention Plan:", prevention)
