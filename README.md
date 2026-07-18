# [Megadodo-Publications](https://megadodo-publications-8e99ae98d78e.herokuapp.com)

Developer: Lisa Scott ([MrsmLisa](https://www.github.com/MrsmLisa))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/MrsmLisa/Megadodo-Publications)](https://www.github.com/MrsmLisa/Megadodo-Publications/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/MrsmLisa/Megadodo-Publications)](https://www.github.com/MrsmLisa/Megadodo-Publications/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/MrsmLisa/Megadodo-Publications)](https://www.github.com/MrsmLisa/Megadodo-Publications)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://megadodo-publications-8e99ae98d78e.herokuapp.com)

Megadodo Publications is a full stack e-commerce web application themed around *The Hitchhiker's Guide to the Galaxy* by Douglas Adams. The site sells books and merchandise from the fictional publishing company Megadodo Publications — the canonical publisher of the Guide itself — as if they were real products you could actually buy.

The idea came from a love of the Hitchhiker's Guide universe and a desire to build something original and creative rather than a generic shop. The site is aimed at fans of the books, science fiction enthusiasts, and anyone who appreciates dry British humour.

The site includes full e-commerce functionality including product browsing, a shopping bag, Stripe payment integration, order history, user profiles, a contact system, and a community forum where users can ask and answer questions.

![screenshot](documentation/mockup.png)

source: [Megadodo-Publications amiresponsive](https://ui.dev/amiresponsive?url=https://megadodo-publications-8e99ae98d78e.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "Boutique Ado".

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide science fiction enthusiasts with a themed e-commerce experience built around The Hitchhiker's Guide to the Galaxy universe.
- Allow users to browse and purchase books and merchandise from the fictional Megadodo Publications.
- Build a community through a forum where users can ask and answer questions.

**Primary User Needs**
- Guest users need to browse products and checkout with ease, without being forced to register.
- Registered users need a streamlined shopping experience with account management and order history.
- Community members need to interact through the forum by posting questions and answers.
- Site owners need tools to manage products, orders, contact messages and forum content through the admin panel.

**Business Goals**
- Drive sales through an engaging and memorable themed shopping experience.
- Build customer loyalty through personalised account features and community interaction.
- Maintain an organised and up-to-date store inventory through the Django admin panel.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Product details including name, price, description, category and images.
- Clear navigation and calls to action for browsing and purchasing.
- Order confirmation pages with full order details.
- Secure payment processing using Stripe.
- User profiles with default delivery information and order history.
- Community forum for questions and answers.
- Contact form for user enquiries.
- 404 and 500 error pages.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Products, Forum, Contact, About and Account sections.
  - Shopping bag icon with running total visible at all times.
  - User icon with dropdown for login, register, profile and logout.
- **Hierarchy**:
  - Featured products on the homepage with clear calls to action.
  - Products listed in a responsive grid with info and add to bag buttons.
  - Forum organised by questions with answers displayed on detail pages.

**User Flow**
1. Guest user browses the shop → views product details → adds to bag.
2. Guest user proceeds to checkout → completes purchase without registering.
3. Registered user logs in → delivery information prefills at checkout.
4. Returning user logs in → views past orders in their profile.
5. Registered user posts a question in the forum → other users answer.
6. User submits a contact message → views message history in their profile.
7. Admin manages products, orders, contact messages and forum content via the admin panel.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

The site uses a strict black and dark navy colour scheme inspired by classic science fiction and the iconic style of the Hitchhiker's Guide itself. The high contrast palette keeps the focus firmly on the product images and content, letting the book covers and merchandise provide the colour.

- `#121933` — dark navy background
- `#ffffff` — white text and card backgrounds
- `#0d111f` — dark navy navbar and footer

![screenshot](documentation/coolors.png)

### Typography

- [Contrail One](https://fonts.google.com/specimen/Contrail+One) was used for all headings, giving the site a bold, slightly retro science fiction feel.
- [Cantarell](https://fonts.google.com/specimen/Cantarell) was used for all body text, providing clean and readable prose.
- [Nabla](https://fonts.google.com/specimen/Nabla) was used for the hero title on the homepage, adding a dramatic dimensional effect.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site for the shopping bag, user icon, social media links and action buttons.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Products | ![screenshot](documentation/wireframes/mobile-products.png) | ![screenshot](documentation/wireframes/tablet-products.png) | ![screenshot](documentation/wireframes/desktop-products.png) |
| Product Detail | ![screenshot](documentation/wireframes/mobile-product-detail.png) | ![screenshot](documentation/wireframes/tablet-product-detail.png) | ![screenshot](documentation/wireframes/desktop-product-detail.png) |
| Bag | ![screenshot](documentation/wireframes/mobile-bag.png) | ![screenshot](documentation/wireframes/tablet-bag.png) | ![screenshot](documentation/wireframes/desktop-bag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile-checkout.png) | ![screenshot](documentation/wireframes/tablet-checkout.png) | ![screenshot](documentation/wireframes/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile-checkout-success.png) | ![screenshot](documentation/wireframes/tablet-checkout-success.png) | ![screenshot](documentation/wireframes/desktop-checkout-success.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| Forum | ![screenshot](documentation/wireframes/mobile-forum.png) | ![screenshot](documentation/wireframes/tablet-forum.png) | ![screenshot](documentation/wireframes/desktop-forum.png) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact.png) | ![screenshot](documentation/wireframes/tablet-contact.png) | ![screenshot](documentation/wireframes/desktop-contact.png) |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |


## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. |
| As a guest user | I would like to add items to my bag and checkout without registering | so that I can complete my purchase quickly. |
| As a guest user | I would like to view product details including description, price and image | so that I can make an informed decision about my purchase. |
| As a guest user | I would like to search for products by name or description | so that I can quickly find what I am looking for. |
| As a guest user | I would like to see a 404 error page if I get lost | so that it is obvious I have stumbled upon a page that does not exist. |
| As a customer | I would like to add items to my shopping bag | so that I can collect products before checking out. |
| As a customer | I would like to view and manage my shopping bag | so that I can review, update quantities or remove items before checkout. |
| As a customer | I would like to proceed to checkout with my bag items and total clearly displayed | so that I know exactly what I am paying for. |
| As a customer | I would like to securely enter my card details using Stripe | so that I can feel confident my payment information is protected. |
| As a customer | I would like to receive an order confirmation page after my purchase | so that I know my order has been successfully placed. |
| As a customer | I would like to get free delivery on orders over €50 | so that I am rewarded for larger purchases. |
| As a registered user | I would like to create an account | so that I can access order history and save my delivery information. |
| As a registered user | I would like to log in and out easily | so that I can access my account securely. |
| As a registered user | I would like the checkout to prefill with my saved delivery information | so that future purchases are quicker and easier. |
| As a registered user | I would like to view my past orders | so that I can track my previous purchases. |
| As a registered user | I would like to update my default delivery information | so that I can keep my profile up to date. |
| As a registered user | I would like to submit a contact message | so that I can get in touch with the team. |
| As a registered user | I would like to view and manage my contact messages | so that I can edit or delete them if needed. |
| As a registered user | I would like to post a question in the forum | so that I can get help from the community. |
| As a registered user | I would like to answer other users questions in the forum | so that I can contribute to the community. |
| As a registered user | I would like to edit or delete my own questions and answers | so that I can manage my forum contributions. |
| As a site owner | I would like to manage products through the admin panel | so that I can add, edit and delete products and categories. |
| As a site owner | I would like to view all orders placed on the site | so that I can track and manage customer purchases. |
| As a site owner | I would like to view all contact messages | so that I can respond to customer enquiries. |
| As a site owner | I would like to moderate the forum | so that I can manage questions and answers across the site. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Navbar | Responsive navbar with links to all main sections, user dropdown, and shopping bag icon with running total. | ![screenshot](documentation/features/navbar.png) |
| Product List | Users can browse all available products in a responsive grid with search functionality. | ![screenshot](documentation/features/product-list.png) |
| Product Search | Users can search for products by name, description or author. | ![screenshot](documentation/features/search.png) |
| Product Detail | Displays detailed information about a selected product including name, description, price and image. Users can select quantity and add to bag. | ![screenshot](documentation/features/product-detail.png) |
| Add to Bag | Users can add items to their shopping bag directly from the product list or detail page. | ![screenshot](documentation/features/add-to-bag.png) |
| Shopping Bag | Users can view the contents of their bag, update quantities and remove items. Running total displayed in navbar. | ![screenshot](documentation/features/bag.png) |
| Free Delivery | Orders under €50 incur a flat €4.99 delivery fee. Orders over €50 receive free delivery. | ![screenshot](documentation/features/delivery.png) |
| Checkout | Users can proceed to checkout providing delivery details and payment information via Stripe. Delivery info prefills for logged in users. | ![screenshot](documentation/features/checkout.png) |
| Stripe Payments | Secure payment processing via Stripe with real-time card validation and webhook handling. | ![screenshot](documentation/features/stripe.png) |
| Order Confirmation | Users see a full order summary page after a successful purchase. | ![screenshot](documentation/features/order-confirmation.png) |
| Toast Notifications | Clear Django messages shown as toast notifications for all user actions including bag updates and checkout. | ![screenshot](documentation/features/toasts.png) |
| User Profile | Registered users can manage their default delivery information. | ![screenshot](documentation/features/profile.png) |
| Order History | Registered users can view all past orders with full order details. | ![screenshot](documentation/features/order-history.png) |
| Forum | Registered users can post questions, answer others questions, and edit or delete their own contributions. | ![screenshot](documentation/features/forum.png) |
| Contact | Users can submit contact messages which are stored in the database and viewable in their profile. | ![screenshot](documentation/features/contact.png) |
| About | Information page about Megadodo Publications written in the style of the Hitchhiker's Guide universe. | ![screenshot](documentation/features/about.png) |
| Delivery Policy | Information about delivery costs and timescales written in the Hitchhiker's Guide style. | ![screenshot](documentation/features/delivery-policy.png) |
| Terms and Conditions | Legal terms written in the style of the Hitchhiker's Guide universe. | ![screenshot](documentation/features/terms.png) |
| Footer | Footer with social media links, developer GitHub and LinkedIn links, and site information links. | ![screenshot](documentation/features/footer.png) |
| 404 Page | Custom 404 error page themed around the Hitchhiker's Guide universe. | ![screenshot](documentation/features/404.png) |
| Admin Panel | Full Django admin panel for managing products, orders, users, contact messages and forum content. | ![screenshot](documentation/features/admin.png) |

### Future Features

- **Email Confirmation**: Send order confirmation emails to users after a successful purchase. Currently configured for console backend only.
- **Product Reviews and Ratings**: Allow customers to leave reviews and rate products with admin moderation.
- **Wishlist**: Enable users to save products to a personal wishlist for future purchases.
- **Discount Codes**: Allow admin to create discount codes for promotions.
- **Extended Product Details**: Add genre, publisher and ISBN fields to product detail pages.
- **Newsletter**: Make a newsletter signup to a real email marketing service such as Mailchimp.
- **PurgeCSS**: Remove unused Bootstrap CSS to improve Lighthouse performance scores.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction including Stripe elements and toast notifications. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online media file storage for product images. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments for e-commerce products. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons throughout the site. |
| [![badge](https://img.shields.io/badge/Google_Fonts-grey?logo=google&logoColor=4285F4)](https://fonts.google.com) | Contrail One, Cantarell and Nabla fonts. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive ERD diagram. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=balsamiq&logoColor=CC0100)](https://balsamiq.com) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Claude-grey?logo=claude&logoColor=D97757)](https://claude.ai) | Help with debugging, troubleshooting and explaining concepts. |
| [![badge](https://img.shields.io/badge/Copilot-grey?logo=githubcopilot&logoColor=000000)](https://github.com/copilot) | Made all the images. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualise database architecture before creating models.

```mermaid
erDiagram
    User {
        int id PK
        varchar username
        varchar email
        varchar password
    }

    UserProfile {
        int id PK
        varchar default_phone_number
        varchar default_street_address1
        varchar default_street_address2
        varchar default_town_or_city
        varchar default_postcode
        varchar default_country
    }

    Category {
        int id PK
        varchar name
    }

    Product {
        int id PK
        varchar sku
        varchar name
        varchar author
        text description
        decimal price
        image image
        int category_id FK
    }

    Order {
        int id PK
        varchar order_number
        varchar full_name
        varchar email
        varchar phone_number
        varchar country
        varchar postcode
        varchar town_or_city
        varchar street_address1
        varchar street_address2
        datetime date
        decimal delivery_cost
        decimal order_total
        decimal grand_total
        text original_bag
        varchar stripe_pid
        int user_profile_id FK
    }

    OrderLineItem {
        int id PK
        int quantity
        decimal lineitem_total
        int order_id FK
        int product_id FK
    }

    Contact {
        int id PK
        varchar name
        varchar email
        varchar subject
        text message
        datetime created_at
    }

    Question {
        int id PK
        varchar question
        datetime created_at
        int created_by_id FK
    }

    Answer {
        int id PK
        text answer
        datetime created_at
        int question_id FK
        int created_by_id FK
    }

    User ||--|| UserProfile : has_one
    User ||--o{ Order : places
    User ||--o{ Question : posts
    User ||--o{ Answer : posts
    UserProfile ||--o{ Order : has_many
    Category ||--o{ Product : has_many
    Order ||--o{ OrderLineItem : has_many
    OrderLineItem }o--|| Product : contains
    Question ||--o{ Answer : has_many
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVk2P2jAQ_SuRz-wqZEMKuVVUlapt1e2hlwopMvYQ3E3srD92lwL_vc4nJCGQ5YCcmeeZ5zczTvaICAooRCC_MBxLnK64Y3-_FUhnX67zH-PaYdR5ejyZXrEkWywdY6Ecp9D3QIpZ0jdnWKk3IWnpOa74KeWTFBuWwMjMFDbYJDrKtoJDxE26BjmMUloC6AhTKkGp6VigNwzU4o1HQkaE6d0VdkLpXORhBBGGa7nr6LHEGmIhdyPFOJWgiWDVpIbokQHUs7kW9dyKjd6KM6k1vGt7GkUkyzQT_OShQFiKEyeTjJwFsrYYyv82N1IdOrIkvz52zvNT0tFdKXLsYE9sTJJEH2vaqz3WqmBr22DxrzfPzWYdbFJqFdQshWLRLwSFhL2CFZhYZn13KZsWGid9p70eOO06i9oLyWLGcRKtcXyRK8sgyhhtly6_OaKsHPnhgn9nHL5pSG8UPje9GMx1S8-aemKDMBukyz7fVZ75LH_tyMr5uUhtKbjGo2frQ62mzPovEN2ROLVlbo1LU2giwS5phHWH4y8DKh_HkSRfKviIFM24Vvb15YH9zNXbzYktTocL5Acy12Qv1e0Gq-Lddjjc3R0OrZdO6GyxiuyYd2BiX908oZMlmIDq-xulw2LiLyAqKXr-OnknUc4kxXzXeRVUqPpi7-LK3eehmuG5CG28R1GocYpL8vZmXHUaqXuYOiaaoFgyikItDUxQCtK2tn1ERelXSG_BDgAK7ZJi-bxCK360ezLM_wiR1tukMPEWhRucKPtksrwJqq-SxiqBW-LL_L5Foe8GRRAU7tE7Cqez4H7uebNF8MmdLqYzb4J2KHzw7n3XC9xgGjx4vnUcJ-hfkdW9n8_miyDw_bnr-wt3Np0goEwL-aP8KCq-jY7_AXq020M)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/MrsmLisa/Megadodo-Publications/projects) served as an Agile tool for this project. User stories were created as GitHub Issues and tracked through a Kanban board with columns for To Do, In Progress and Done.

![screenshot](documentation/agile/kanban.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/MrsmLisa/Megadodo-Publications/issues) were used to create and track user stories throughout the project.

![screenshot](documentation/agile/issues.png)

### MoSCoW Prioritisation

User stories were prioritised using MoSCoW notation:

- 🔴 **Must Have** — core e-commerce functionality, authentication, Stripe payments
- 🟡 **Should Have** — user profiles, order history, forum, contact
- 🟢 **Could Have** — future features listed above

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found at [Megadodo Publications](https://megadodo-publications-8e99ae98d78e.herokuapp.com).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain your own PostgreSQL Database from Code Institute, follow these steps:

1. Sign in to the CI LMS using your Code Institute account.
2. An email will be sent to you with your new Postgres Database.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are deleted after 18 months.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store product images online since Heroku does not persist file storage.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose "Programmable Media for image and video API".
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle all e-commerce payments.

Once you've created a Stripe account and logged in, follow these steps:

- From your Stripe dashboard, click **Developers**, and select **API Keys**.
- You'll have two keys here:
  - `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
  - `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

For Stripe Webhooks:

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- Click **Add Endpoint**.
  - `https://megadodo-publications-8e99ae98d78e.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key:
  - `STRIPE_WH_SECRET` = Signing Secret (Webhook) Key (starts with **wh**)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com) for deployment.

Deployment steps:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app**.
- Your app name must be unique. Choose a region closest to you and select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `SECRET_KEY` | user's own value |
| `CLOUDINARY_URL` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*temporary, remove for final deployment*) |

Heroku needs these files to deploy:

- `requirements.txt`
- `Procfile`
- `runtime.txt`

Install requirements:

```bash
pip3 install -r requirements.txt
```

The **Procfile** contains:

```
web: gunicorn megadodo_publications.wsgi
```

To deploy from the terminal:

```bash
heroku login -i
heroku git:remote -a app_name
git push heroku main
```

After deployment run migrations:

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Local Development

#### Cloning

1. Go to the [GitHub repository](https://www.github.com/MrsmLisa/Megadodo-Publications).
2. Click on the green "Code" button and copy the URL.
3. In your IDE Terminal, type:
   - `git clone https://www.github.com/MrsmLisa/Megadodo-Publications.git`

Create a new file called `env.py` at the root level:

```python
import os

os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")
os.environ.setdefault("DEVELOPMENT", "True")
```

Then run:

```bash
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

#### Forking

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/MrsmLisa/Megadodo-Publications).
2. Click the "Fork" button at the top of the repository.
3. You should now have a copy in your own GitHub account.

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project — inspiration for e-commerce structure and Stripe integration |
| [Bootstrap](https://getbootstrap.com) | Various components and responsive front-end framework |
| [Django Documentation](https://docs.djangoproject.com) | Django framework reference |
| [Django Allauth](https://django-allauth.readthedocs.io) | User authentication |
| [Stripe Documentation](https://docs.stripe.com) | Payment integration and webhook setup |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file serving on Heroku |
| [Cloudinary](https://cloudinary.com) | Media file storage |
| [Douglas Adams](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy) | The Hitchhiker's Guide to the Galaxy — theme and creative inspiration |
| [Claude AI](https://claude.ai) | Help with debugging, troubleshooting and explaining concepts throughout the project |
| [GitHub Copilot](https://github.com/copilot) | Code autocompletion during development |

### Media

| Source | Notes |
| --- | --- |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Google Fonts](https://fonts.google.com) | Contrail One, Cantarell and Nabla fonts |
| [Cloudinary](https://cloudinary.com) | Product image hosting |
| Product images | Created by the developer using AI image generation tools |
| Logo | Designed by the developer |

### Acknowledgements

- I would like to thank my Code Institute mentor Tim Nelson for the support and guidance throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging project issues.
- I would like to thank Stephen and Jessica Fransson Duffy, and Fahim for the testing.
- I would like to thank my husband and son for his patience and support.
- I would like to thank Douglas Adams for writing The Hitchhiker's Guide to the Galaxy, without which this project would have been considerably less fun to build. Don't Panic.
