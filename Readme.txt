API paths for peers to test
==========================

Please use these endpoints when reviewing this Little Lemon capstone project.
Test with the Insomnia REST client (or similar) or the DRF Browsable API.

1. Get auth token (POST with username & password):
   /api/api-token-auth/

2. Registration (Djoser):
   /api/registration/users/   (POST to register)

3. Menu (requires authentication):
   /api/menu/

4. Bookings (requires authentication):
   /api/bookings/

Use the token in the Authorization header: "Token <your-token>"
