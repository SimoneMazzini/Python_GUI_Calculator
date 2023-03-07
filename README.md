# Python_GUI_Calculator
Create from the scratch a GUI Calculator based on PyQt5 in Python

In this exercise, you’ll see and develop, if you want, a calculator GUI app using the Model-View-Controller (MVC) design pattern. This pattern has three layers of code, with each one having different roles:

1) The model takes care of your app’s business logic. It contains the core functionality and data. In your calculator app, the model will handle the input values and the calculations.

2) The view implements your app’s GUI. It hosts all the widgets that the end user would need to interact with the application. The view also receives a   user’s actions and events. For your example, the view will be the calculator window on your screen.

3) The controller connects the model and the view to make the application work. Users’ events, or requests, are sent to the controller, which puts the model to work. When the model delivers the requested result, or data, in the right format, the controller forwards it to the view. In your calculator app, the controller will receive the target math expressions from the GUI, ask the model to perform calculations, and update the GUI with the result.

Here’s a step-by-step description of how your GUI calculator app will work:

1) The user performs an action or request (event) on the view (GUI).
2) The view notifies the controller about the user’s action.
3) The controller gets the user’s request and queries the model for a response.
4) The model processes the controller’s query, performs the required computations, and returns the result.
5) The controller receives the model’s response and updates the view accordingly.
6) The user finally sees the requested result on the view.
7) You’ll use this MVC design to build your calculator app with Python and PyQt.
