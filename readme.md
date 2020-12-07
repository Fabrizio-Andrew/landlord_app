# Read Me - Landlord App

Brief outline:

1. **Overview:**  The Landlord App allows users to track rental properties they own and any tenants who live in them.  Users can add, remove, and delete rental units from their account.  They can also add, remove and delete tenants from each rental property.

2. **Technology:** 
- While the login and registration pages are straight HTML, the bulk of the application's front end is written in React.  All front-end logic can be found in unit_list.js.
- The front end also leverages bootstrap for a full mobile-responsive design.
- Back-end processing is managed in views.py.  Generally, the front and back ends are connected via API endpoints.

3. **State Model:** IMPORTANT FOR SET UP
- States are managed as their own data model.  So, it is important that you create a state on the /admin page after migrating models.py.  Any units you create must be associated with a state.  So, it will be impossible to proceed without this step.
- The State model itself is currently under-utilized.  However, the idea is to gather various state laws regarding landlord-tenant rights.  So, the State model will help with long term scalability and sustainability.

4. **Logging In:** The application front end takes an email address for a username.

4. **Dependencies:** The only external dependency is Factory Boy - and this is only used for Unit Tests.  However, I have included a requirements.txt file for good measure.