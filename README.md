# ![MLJ logo](static/favicon-32x32.png) Memory Lane Jewellery

Memory Lane Jewellery is an online jewellery shop that specializes in crafting and curating pieces of sentimental &nostalgic value. My Jewellery is designed to help you create precious memories for you and your loved ones to cherise for a long time. I can offer custom engravings on my pendants and , or designs inspired by personal history. I believe in a sense of emotional connection and the idea that each piece of jewellery is a keepsake with a story behind it, making it a great choice for meaningful gift.

I can offer custom engravings on my pendants and/or designs inspired by personal history. 

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

### !(https://docs.djangoproject.com/en/3.2/ref/models/expressions/#using-f-to-sort-null-values) F Object
Used this along with nulls_last on descending sort when Ratings field has null

#### Checkout

##### Stripe currency & Pricing

The currency is set to Euro in settings.py as all goods are for sale from Ireland.  Stripe requires all Euro amounts to be provided in cents, cents being the smallest Euro unit.  In keeping with the business strategy of whole number pricing,  it was necessary to round up `grand_total` & `stripe_total` using `math.ceil()` when including delivery costs.


#### Product Pricing
It is a strategic business decision to opt for whole number pricing in order to maintain the feeling of exclusivity and quality in the goods.  The discerening customer would not fall for the charm pricing of say €49.99.

#### Stripe Secrets

Use `<input type="hidden"..>` to pass the `client_secret` to stripe server, With the hidden attribute set the user cannot view or interact with the value being passed

##### Redundancy for payment system on chekcout app

There is redundancy build into the Checkout app during Stripe payment processing in cases where the user might close the browser or lose power/connectivity or do something on the client/frontend side that breaks connection with the server during payment processing causing the order not to be submitted to the database even though the payment has been made. This is for edge cases only and is achieved by listening for particular stripe webhooks (wh's) which operate like signals in the background and are unaffected by whats going on front end. It is the same implementation as **BoutiqueAdo**. The Stripe account is configured to send wh's to an endpoint such as `https://memorylane-jewellery-63c74e421293.herokuapp.com/checkout/wh/`. A `payment_intent.succeeded` webhook is send by Stripe to signify that the payment has been completed. 
 & once a wh is verified as 

 When a `payment_intent.succeeded` webhook is send by Stripe it signifies that the payment has been made, 


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




## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
