# Storylab
A writer's workshop

For the last 2 years I’ve been a full-time screenwriter. A huge amount of that work involves story brainstorming, creating simple one or two sentence story ideas. It’s extremely time consuming, but with an app that breaks down stories into their basic elements, it can be accomplished in moments. 
All stories are comprised of a few basic components. A character who desires something and fears something, the obstacles that stand in their way, the consequences if they fail, and the rewards if they succeed. 
I want to build an app that allows the user to create, read, update, and delete  story seed objects constructed from an array of characters, desires, fears, obstacles, consequences, and rewards. With the additional feature of an AI component, this seed will be planted into a chatbot (using openai) prompted to return a fully realized story treatment. 

# User Stories

As a user, I should be able to register a new account for Storyteller’s Garder
Given the user wants to use Storyteller’s Garden
And does not have an account
When the user clicks on the Register link at the bottom of the login form
Then a registration form will be presented

As a user, I should be able to make a story seed
Given the user wants to create a story seed
When the user navigates to the SEEDS page and clicks NEW SEED
Then they are navigated to a CREATE SEED FORM

As a user, I should be able to complete a story seed
Given the user wants to complete a story seed
When the user fills out the SEED FORM and clicks CREATE
Then they are navigated back to the SEEDS page where their new story seed can be read


As a user, I should be able to update my story seed
Given the user wants to update a story seed
When the clicks UPDATE next to their displayed story seed
Then they are navigated to the UPDATE SEED FORM

As a user, I should be able to complete my updated story seed
Given the user wants to complete an update to a story seed
When the user makes changes to the UPDATE SEED FORM and clicks UPDATE
Then they are navigated back to the SEEDS page where their updated story seed can be read

As a user, I should be able to delete my story seed
Given the user wants to delete a story seed on the SEED PAGE
When the user clicks DELETE next to the selected story seed
Then the seed object is deleted from the database


