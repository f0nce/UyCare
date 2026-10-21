# YouTrack setup and import

No YouTrack instance or project has been created in this package. The team must create or supply an accessible instance using its own accounts. Suggested project name: UyCare. Suggested key: UYC, subject to availability.

1. Create the project and invite the three students and supervisor with suitable permissions. Map the supplied full names to real user accounts. Avoid creating pretend assignees.
2. Configure Task, priorities Critical/High/Normal, states Open/In progress/Review/Done, Assignee and Due Date. Use the project's equivalent values if its defaults differ.
3. Upload management/youtrack-backlog.csv to Google Sheets, then use the documented YouTrack Google Sheets/CSV import workflow [S23]. Review the preview, field types and date parsing before committing the import. This CSV is a staging format, not proof of completed import.
4. Assign actual users and verify each acceptance criterion and due date. Update proposed dates to the official calendar. Record the resulting real IDs in management/task-id-map.md.
5. Replace the missing YouTrack link in README and connect the repository integration if available. Use the real IDs in subsequent branch names and PR/commit descriptions.
6. Add links from each issue to its PR or deliverable. Move to Done only after review and acceptance evidence.

Official import guidance: https://www.jetbrains.com/help/youtrack/cloud/import-from-csv.html

The first import should keep every issue Open. Prepared documents can then move to Review after a member accepts ownership. Do not import the assistant's generated files as evidence of independent student contributions.
