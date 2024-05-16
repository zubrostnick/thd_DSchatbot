Domain Specific chatbot, that follows the GCD process. Created as part of THD Assistance Systems course.

## Project description
THDfund.Students often face various money-related challenges during their academic journey, that can impact their academic experience. Our chat bot serves to help to solve some common money-related problems that students may encounter throughout their academic journey. Primary objective of the THDFund bot is to provide information concerning personalal user requests. The domain is quite important and the usage field is quite extencive. More could be read in the project's WIKI.

## Prerequisites
Python 3.9.7; Rasa 3.6.15; Flask 3.0.0; scikit-learn 1.1.3;
A full list of prerequisites could be found in "[requirements.txt](https://mygit.th-deg.de/rz28551/my_first_project/-/blob/main/requirements.txt)" (also see 'Installation')

## Installation and getting started
- Download the repository
- Create and activate virtual environment on your system
- `pip install -r requirements.txt` - use this command to install the dependencies needed for the project work. This should be done in the root of the folder
- set FLASK_APP=app.py
- set FLASK_ENV=development
- flask run (- terminal 1)
- `rasa run actions` - start the action server (for custom actions) (- terminal 2)
- Rasa assistant is started witht he `rasa shell` command  (- terminal 3)

## Basic Usage:
After installation and setting up you are ready to use the bot. To set off with bot's usage, greet first by saing (hi, hello, etc.). Bot is already ready to assist you in numerous of usecases:  
- Tuition scholarships in THD
- Tuition Fees + Tution reregistration (+documents)
- Answering most popular question related to Part-time/Full-time job search in Deggendorf
- Living expences in Deggedorf, providing helpful information

You can always reach for help by explicitly stating this intent in various ways (ex. I need help, help). All the steps and bot's suggestions are sufficient enough to lead the conversation naturally without any need to use documentation for some concrete requests. In case you want to finish conversation abruptly write terminate intent. You may also don't want to continue, when bot answers your question. It will ask you whether you want to continue, or you need anything else to know about (he will not greet again, each time it answers your question), you may finish your conversation here, by negation, or explicit quit intent. In case it was done by mistake, you will be asked reassurance questions (as a part of fallback mechanism, or "are you sure?" type questions); so you can always avoid undesired behavior. You can continue using bot seamlessly as much as you need.



## Implementation of Requests
The conversational design started with the 'Right Fit' according to Google's conversation design. then the personas and relatable use cases were defined. Afterwards, sample dialogs for each of use cases were defined, which was the foundation for the conversation flow build. Rasa implemenation part handles the majority of designed use cases. "Girokonto", "Studying abroad funding" were excluded from implementation due to their limited additional value, in terms of new approaches and significant features implementation that are already efficiently covered by Rasa's existing tools in other use cases. 
- **nlu.yml** - Handles intent classification, describes 26 user intents, handles enity recognition (and assigns the values to the declared slots); declares synonyms for scholarship_choice entity's values. The NLU model uses this data to understand user messages and extract relevant information.
- **domain.yml** - The domain file defines the chatbot's universe, including intents, entities, slots (bot's memory, which stores user input), actions (responses, utterances, custom actions). It specifies what the assistant can understand and say.
- **rules.yml** - Rules describe short pieces of conversations (small specific conversation patterns) that should always follow the same path. Start and termination of the conversation of the communtication with bot as well as two-stage fallback are implemented in this file.
- **stories.yml** - This part implements 16 stories, what the chatbot's conversation will be based on. Basically, this is the main part of our conversationflow. 
- **config.yml** - This file contains the configuration of the Rasa NLU pipeline and the policy ensemble for dialogue management. It defines the processing pipeline for user messages and the policies that decide the next action in a conversation. Allows us to use stories, handle fallbacks, perform minor adjustments for the sake of bot's effectiveness improvement.
- **actions.py** - This files contains our 6 custom action, which allow for dynamic and context-aware responses, making the conversation with the bot more interactive and personalized. These actions handle API calls (flask), cutomization of responses based on the conversation context (slot handling actions)
- **endpoints.yml** - minor changes in this file allow us to define endpoints for custom actions
- **app.py** - Data services were implemented with Flask framework in app.py. Provides an API with two endpoints to interact with the scholarships data. The data is initially loaded from a JSON file named 'tuition_scholarships.json' which contains inormation for personalized custom responses via custom actions.



