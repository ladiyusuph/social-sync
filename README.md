# SocialSync

SocialSync is a social media platform developed using Django, where users can connect with each other, share posts, and interact with content.

## Features

- User authentication: Users can sign up, log in, and log out.
- User profiles: Each user has a profile page where they can upload a photo and provide additional information.
- Following system: Users can follow and unfollow other users to see their posts in their feed.
- Post feed: Users can view a feed of posts from users they follow.
- Posting images: Users can upload images to share with their followers.
- Actions feed: Users can see a feed of actions, including posts and image uploads from users they follow.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ladiyusuph/socialsync.git
```

2. Navigate to the project directory:

```bash
cd socialsync
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Sign up for a new account or log in with an existing one.
- Complete your profile by uploading a photo and providing additional information.
- Explore other users and follow them to see their posts in your feed.
- Upload images to share with your followers.
- Interact with posts by liking and commenting on them.
- Stay updated with the actions of users you follow in your actions feed.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```