# Test-driven Development

TDD is a software development process relying on software requirements beign converted to test cases before software is fully developed and tracking all software development by repeatedly testing the software against all test cases.

The process is related to the test-first programming concepts of extreme programming, begun in 1999, but recently has created more general interest in its own right.

Is used to create a test before the code developed.

## ***TDD Cycle:***

    - 1️⃣. Add a test:

        - "Add a check" replaces "Add a test"

    - 2️⃣. Run all tests and see if the new test fails:
        
        - "Run all checks" replaces "Run all tests"

    - 3️⃣. Write the code:

        - "Do the work" replaces "Write some code"

    - 4️⃣. Run tests:

        - "Run all checks" replaces "Run tests"

    - 5️⃣. Refactor code:

        - "Clean up the work" replaces "Refactor code"

    - 6️⃣. Repeat 🔁

## ***TDD Best Practices:***

    - 1️⃣. Test structure:

        - Setup;
        - Execution;
        - Validation;
        - Cleanup;

    - 2️⃣. Individual best practices:

        - Separate common set-up and tear-down logic into test support services utilized by the appropriate test cases.

    - 3️⃣. Practices to avoid, or "anti-patterns":

        - Slow running tests;
        - Testing implementation details;
        - Testing precise execution behavior timing or performance;
        - Dependecies between test cases;


