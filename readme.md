<h1>Hello guys this is my First BIG PROJECT</h1>

Its typically a website which allow user to 

    - Create Rooms For Different Topics
    - Send Messages to Different rooms
    - Login/Signup via Google/Github Account
    - User can search Rooms through 
        - Creater Name
        - Room Name
        - Room Topic
        - Room Description

    
    To View Anyuser's Profile you need to Login First
        - Only then you can see other's Profile
        - Can send Messages to Rooms
        - Can create Room


    After Login And Creating Room User can Edit Room's Details,Delete Room


    User can Delete their Recent Activity 
        - Created Room
        - Send Messages
        via Recent Activity Tab


    Most Recent Activity will appear on the Top

------------------------------------------------------------------------------------------------------------------

<h1>All Methods/Notes are written on files</h1>

<h2>I followed DENIS IVY tutorial to create this Project but in many places i used my own methods</h2>

I hope this Project will Help you in your Learning Journey...

Happy Coding

And Please forgive me if you found any Grammatical Mistake in my English. 


------------------------------------------------------------------------------------------------------------------


<h2>Major Problems Encountered while Doing this Project</h2>

**First**: Custom User Model Implementation
- Initially, I observed that Dennis Ivy implemented a Custom User Model using `AbstractUser`.
- However, I opted to create an additional model named `UserProfile` to incorporate features like bio and profile picture functionality. This model establishes a one-to-one relationship with the user model.

**Second**: Handling Signups via Google/Github
- An issue arose when users signed up via Google/Github, as their `UserProfile` was not populated, causing errors.
- To address this, I leveraged Django's signal features. Now, whenever a user signs up through Google/Github, a new object is created in the `UserProfile` model automatically.

**Third**: Managing the One-to-One Relationship
- Another challenge I encountered was managing the one-to-one relationship between the user and `UserProfile` models.
- To ensure seamless integration, I ensured that when a user signs up, their data is appropriately related to the `UserProfile`.



