mindlancer-project/
├── 🖥️ Frontend (Next.js) - User Interface/
│   ├── public/                 # Static files
│   │   └── assets/            # Images/icons/fonts
│   │
│   ├── src/                    # Source code
│   │   ├── components/         # Reusable pieces (Buttons, Cards)
│   │   ├── pages/              # Website pages
│   │   │   ├── auth/           # Login/Signup pages
│   │   │   ├── dashboard/      # User dashboard after login
│   │   │   └── index.js        # Homepage
│   │   │
│   │   ├── services/           # API connection files
│   │   │   ├── api.js          # Setup for API calls (Axios)
│   │   │   └── auth.js         # Login/Signup API functions
│   │   │
│   │   └── styles/             # CSS/SCSS files
│   │
│   └── package.json            # Frontend dependencies
│
└── 🛠️ Backend (Django) - Server & Database/
    ├── mindlancer/             # Project configuration
    │   ├── settings.py         # Database/security settings
    │   └── urls.py             # URL paths → API endpoints
    │
    ├── users/                  # User accounts system
    │   ├── models.py           # Database tables for users
    │   ├── views.py            # API: Registration/Login
    │   └── admin.py            # Admin panel controls
    │
    ├── jobs/                   # Job listings system
    │   ├── models.py           # Database table for jobs
    │   └── views.py            # API: Create/Search jobs
    │
    ├── proposals/              # Freelancer applications
    │   ├── models.py           # Database for proposals
    │   └── views.py            # API: Submit/manage proposals
    │
    └── manage.py               # Start server/run commands