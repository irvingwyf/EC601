# EC601
# For Phase 1 (a), our goal is to practise and learn about twitter APIs.
# I wrote 5 test programs and tried in total 13 different test programs including the one given in class.
# I have tested the following functionalities including filtered-stream that contains methods to add, 
# remove, and retrieve rules from my stream; retrieving direct message including the status of the specific
# message indentified by ID; uses bearer token to authenticate and retrieve the specified Tweet objects by
# their IDs; the recent research that uses bearer token to authenticate and make a Search request; sampled
# stream that connects to the Sample stream endpoint and outputs data; get tweets that uses bearer token to
# authenticate and retrieve the specified Tweet objects by ID; get tweets with user context that implements
# the PIN-based OAuth flow to obtain access tokens for a user context request, then makes a Tweet lookup 
# request by IDs with OAuth 1.0a authentication of user context; user lookup that uses bearer token to 
# authenticate and retrieve the specified User objects by ID; get users with user context that implements the
# PIN-based OAuth flow to obtain access tokens for a user context request, then makes a User lookup request 
# by usernames with OAuth 1.0a authentication of user context.
# For most of the test programs they ran without issue, and the ones that need to implement the authentication
# will give the link when running using terminal and then by going to the link on browser, we can get the one
# time generated pin code, then by input the code inot terminal can access the further operation. However,
# also most of the API functions can be test and demonstrate once we got the access token, secret, consumer 
# token and secret, bearer token, there are some APIs that I cannot try out and test, for example the APIs
# that involving direct message, I am not sure if it is because my twitter account is newly applied and thus
# there is no direct message to test, or it is a general thing that certain API methods are not allowed to
# editing, delete or create direct messages due to lack of access.
# Over all, the twitter APIs uses IDs to label and track each and every operation in their system including
# every tweet has its own ID that can be used to locate and retrieve information about it by users or the
# administrator(assuming there is one which makes sense), and in order to visit or view or use any data, the
# Oauth will be used that require users to use their own tokens as the key to access these contents and also
# it can be used to reversely tracking down who visited certain things by locating and recognizing their
# unique tokens.
# Although I have heard a lot about twitter, this is the first time I tried to understand and even tryout some
# of the APIs and the functions within twitter application, and I am impressed.






