![Am I responsive](media/docs/amires.JPG)

# ![MLJ logo](static/favicon-32x32.png) Memory Lane Jewellery

### About 

Memory Lane Jewellery is a fictional online jewellery store selling handmade jewellery.  All pieces are designed and carefully crafted by master goldsmith Siobhan O'Brien. She has created a range of jewellery that can be of sentimental & nostalgic value to whomever wears it.  Each is designed to help create precious memories,  mark milestones & is made from highest quality precious metals for you to enjoy over a lifetime & cherish as family heirlooms.
Message from Siobhan
I can offer custom engravings on my rings & pendants.  Please contact xxx-xxx-xxxx to arrange.

### B2C

This is a business to customer application.  There are several products and a single payment per order. Customers can purchase anonymously or can register for an account in which case they can safe their delivery informaiton &/or subscribe to a quarterly newsletter.  PAyment is via Stripe & banking details are held or saved.


Memory Lane Jewellery is a fictional online jewellery store selling handmade jewellery.  All pieces are designed and carefully crafted by master goldsmith Siobhan O'Brien. She has created a range of jewellery that can be of sentimental & nostalgic value to whomever wears it.  Each is designed to help create precious memories,  mark milestones & is made from highest quality precious metals for you to enjoy over a lifetime & cherish as family heirlooms.
Message from Siobhan
I can offer custom engravings on my rings & pendants.  Please contact xxx-xxx-xxxx to arrange.

### !(https://docs.djangoproject.com/en/3.2/ref/models/expressions/#using-f-to-sort-null-values) F Object
Used this along with nulls_last on descending sort when Ratings field has null

### UX
#### Wireframes




#### Checkout

##### Stripe currency & Pricing

The currency is set to Euro in settings.py as all goods are for sale from Ireland.  Stripe requires all Euro amounts to be provided in cents, cents being the smallest Euro unit.  In keeping with the business strategy of whole number pricing,  it was necessary to round up `grand_total` & `stripe_total` using `math.ceil()` when including delivery costs.


#### Product Pricing
It is a strategic business decision to opt for whole number pricing in order to maintain the feeling of exclusivity and quality in the goods.  The discerening customer would not fall for the charm pricing of say €49.99.

#### Stripe Secrets

Use `<input type="hidden"..>` to pass the `client_secret` to stripe server, With the hidden attribute set the user cannot view or interact with the value being passed

##### Redundancy for payment system on chekcout app

There is redundancy build into the Checkout app during Stripe payment processing in cases where the user might close the browser or lose power/connectivity or do something on the client/frontend side that breaks connection with the server during payment processing (the js .done .then on 'stripe.confirmCardPayment') causing the order not to be submitted to the database even though the payment has been made. This is for edge cases only and is achieved by listening for particular stripe webhooks (wh's) which operate like signals in the background and are unaffected by whats going on front end. It is the same implementation as **BoutiqueAdo**. The Stripe account is configured to send wh's to an endpoint such as `https://memorylane-jewellery-63c74e421293.herokuapp.com/checkout/wh/`. A `payment_intent.succeeded` webhook is send by Stripe to signify that the payment has been completed.  Therefore if/when that particular wh is received we know for definite that payment has been made & in normal cases the order will already have been created by `views.checkout` (abeit a slight delay in writing to db using false commit on the save `order_form.save(commit=False)`).  However in an edge case where something happens frontend so that order never gets created in the db, the `payment_intent.succeeded` wh handler will create the order if it finds that it does not exist in the db.  There is a boolean field on the Order model called 'CreatedByWebhook` to track such cases.  The site administrator can check for this phenomena using filter on the django admin interface.

 
#### Responsive

The delivery banner (`#delivery-banner`) not displayed on screens < 480 px 

### Deploy

- Create a Database eg Elephant SQL
- Create a new Heroku app
- Connect the db to local development server
- Confirm DB is connected
- first deploy with debug off & disable collect static
- upload media to s3 & grant public access
- create new stripe webhook endpoint (url for heroku app)
- reveal and add webhook signing secret to heroku config vars matching var names in settings.py


 Deployment 
- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab.
  - Open the pages tab on the left hand side of the page.
  - From the source section drop-down menu, select the Master Branch.
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
<!-- Deployment code and content taken straight from Code Institutes README template -->

- You can view the live site 

### Credits
#### Images taken from https://www.cooksongold.com/

#### Last page of LMS
Important information regarding your E-Commerce Applications Portfolio Project
Congratulations on completing the Boutique Ado walkthrough project!

As indicated prior to the Boutique Ado walkthrough project, the following ‘Introduction to Search Engine Optimization’ and ‘Web Marketing’ modules contain important information that will be required for your final portfolio project.

Concepts that will be required for your final project include:

SEO implementation, including:
A robots.txt file
A sitemap.xml file
Descriptive meta tags
rel attributes on links to external resources
Marketing techniques, including:
The need for the creation of either a real Facebook business page, or a mockup of one.
A newsletter signup form, either through a service such as MailChimp or through a custom implemented one.
The requirements for an e-commerce business model:
The necessity for the inclusion of an e-commerce business model, highlighting the purpose of the application as either B2B or B2C focused, and detailing the core business intents and marketing strategies for the application.
Questions to ask yourself:
What do your users need?
What information and features can you provide to meet those needs?
How can you make the information easy to understand?
How can you demonstrate expertise, authoritativeness and trustworthiness in your content?
Would there be other pages within your own site you could link to from your chosen page?
Are there opportunities to link back to external websites that already rank highly on Google?
How can you help users discover other relevant parts of your web application?
Tips
Research other sites that already meet the needs your users have, find examples of how they accomplish that.
Use the keyword list you created in the Keyword challenge to help prompt further ideas
Document your process. If you’re planning for your final project, keep this documentation for your README.


### marketing
Marketing Types Challenge
In our last videos, we explained some of the pros and cons of each marketing type, and we talked about which businesses they suit.

In this unit we’re going to challenge you to use what you have learned and plan which marketing types to use for an ecommerce business.

Using the ecommerce business idea you chose for the keywords and content challenges:
Your own project idea (possibly for your final project)
A pizza restaurant, based in Dublin, that takes online orders for delivery.
Plan out which marketing types you think would work best for your chosen business. Jot down which ones you think the business would benefit from using, and why.

Questions to ask yourself
Who are your users?
Which online platforms would you find lots of your users?
Would your users use social media? If yes, which platforms do you think you would find them on?
What do your users need? Could you meet that need with useful content? If yes, how could you best deliver that content to them?
Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?
What are the goals of your business? Which marketing strategies would offer the best ways to meet those goals?
Would your business have a budget to spend on advertising? Or would it need to work with free or low cost options to market itself?
Tips
Research other ecommerce businesses that sell similar products or services to your idea. What marketing practices do they employ? Which ones appear to be working best?
Document your process. If you are planning for your final project, keep this documentation for your README.

#### Bugs

#### Favicon

The favicon has not rendered on the deployed version & still trying to correct this at writing.   It did appear on the development sever 

#### 404

