# Grazioso-Salvare-Animal-Shelter-Dashboard
The project includes setting up MongoDB, managing animal data, creating CRUD functionality in Python, and developing a dynamic dashboard with interactive filtering options. The final dashboard displays rescue-related information, maps, and charts.

**1. Writing Maintainable, Readable, and Adaptable Programs**

Keep things modular: Break your code into small, focused parts (like the CRUD module). Each part handles one job—this makes your code easier to understand, test, and update later.
Use clear names and comments: Good naming for functions and variables tells others (and your future self) what your code is doing. Brief, meaningful comments can save a lot of confusion down the road.
Reuse code: When you separate out a CRUD module, you can drop it into future projects without rewriting all the database code. That means faster development and fewer bugs.

**2. Advantages of the CRUD Python Module & Future Use**

Simplicity: The dashboard code doesn’t need to worry about how the database works. It just calls the CRUD functions (e.g., read({})) and gets results.
Testing: You can test each CRUD function separately. If it works, you know the database part is solid, and you can focus on testing your dashboard or other features.
Future projects: If you build another app, you can reuse the same CRUD module to connect to the same database. You could also adapt it to other databases or turn it into a web API.

**3. Approaching a Problem as a Computer Scientist**

Understand the requirements: For Grazioso Salvare, we needed a dashboard to view, filter, and visualize animal data. Knowing exactly what the client needs is the first step.
Plan the data flow: Decide how data will be stored (MongoDB documents), how it will be accessed (CRUD module), and how it will be displayed (Dash).
Build iteratively: Start with something simple (a basic table), then add new pieces one by one (pie chart, map, filters). Test each step and refine.
Learning from other projects: This project combined both front-end and back-end work. That might be different from smaller coding exercises in other classes, but it’s closer to real-world scenarios where you handle everything from the database to the user interface.

**4. Future Database Strategies**

Design the schema carefully: Think about how data will be used. If filtering by rescue type is key, make sure that field is stored in an easy-to-query format.
Plan for growth: If you expect more data or new features, keep your design flexible (e.g., indexing, relationships between tables or documents).
Keep security in mind: Real-world apps need robust permissions, authentication, and safe ways to handle sensitive data.

**5. What Do Computer Scientists Do, and Why Does It Matter?**

Problem-Solving: Computer scientists figure out efficient ways to handle complex data, automate tasks, and create user-friendly tools.
Real Impact: For a company like Grazioso Salvare, a well-made dashboard saves time, reduces errors, and helps them organize rescues more effectively. This could improve rescue outcomes and even save lives.
Data-Driven Decisions: By turning raw data into clear charts and maps, companies can spot trends, identify gaps, and take action based on real insights.

# PROJECT STEPS
**1. Accessing MongoDB Through the Terminal**

Prerequisites:

      1.	Download and Install MongoDB:
          o	MongoDB Community Edition
          o	MongoDB Compass for GUI operations.
          
      2.	Required Tools:
          o	Python 3.x
          o	Jupyter Notebook (with required libraries installed).
          
**Steps to Access MongoDB:**

      1. Start MongoDB service:
            bash
            Copy code
            sudo service mongod start
            a. Connect to MongoDB:
                bash
                Copy code
                mongo --host <host_name> --port <port_number>
             b. Confirm connection status:
                javascript
                Copy code
                db.runCommand({ connectionStatus: 1 })
   
 
3. Importing the AAC Database

Task: Import the Austin Animal Center (AAC) Outcomes dataset as the animals collection in the AAC database.
Import and Execution

Task: Import the AAC Outcomes CSV file into MongoDB using the mongoimport tool, specifying the database name as "AAC" and the collection name as "animals". Provide screenshots of the import command and its   successful execution.
•Output of the mongoimport command in the Linux terminal showing the command used to import the CSV file.
•Terminal output confirming successful data import, including the number of documents imported.

<img width="468" alt="image" src="https://github.com/user-attachments/assets/db4b00dc-9930-4c52-80a7-f62b70f0b298" />

<img width="468" alt="image" src="https://github.com/user-attachments/assets/0dc6c058-bdd4-44bb-b937-549bd0abe686" />

   
 
5. Simple Index and Explain Function
Task: Create a simple index on the key "breed" in the "animals" collection of the "AAC" database. Show an example query using this index and use the explain() function to verify that the index is being used. Provide screenshots of the index creation, the query, and the explain() output.
Screenshots and Explanations
•	Command in the mongo shell creating the simple index on "breed".
•	Example query using the "breed" index (e.g., finding all animals with a specific breed).

<img width="468" alt="image" src="https://github.com/user-attachments/assets/0aa2316d-7ccd-4eff-a8ac-a52385026d6d" />
•	Output of the explain("executionStats") function showing that the index is used in the query execution plan.

<img width="468" alt="image" src="https://github.com/user-attachments/assets/f2a6875f-f7f1-4158-b005-08543b9e6ed6" />

  
4. Compound Index and Explain Function
Task: Create a compound index on "breed" and "outcome_type" to improve the performance of queries looking for breeds with an "outcome_type" of "Transfer". Show an example query using this compound index and use the explain()function to confirm that the index is being used. Provide screenshots of the index creation, the query, and the explain()output.
Screenshots and Explanations
•	Command in the mongo shell creating the compound index on "breed" and "outcome_type".
•	Example query using the compound index (e.g., finding all animals of a specific breed with an "outcome_type" of "Transfer").

   <img width="468" alt="image" src="https://github.com/user-attachments/assets/9b45e1c0-93ad-481b-b9b6-03bc0886d36e" />

•	Output of the explain("executionStats") function showing that the compound index is used in the query execution plan. 

<img width="468" alt="image" src="https://github.com/user-attachments/assets/23a0fe87-62d0-4e8a-9452-c4c49875fa3f" />

 
5. Ensuring User Authentication
Task: Create a new user account called "aacuser" for the "AAC" database with appropriate roles to ensure user authentication. Verify that both the admin and "aacuser" accounts can access MongoDB and list the databases. Use the db.runCommand({connectionStatus:1}) command to confirm the connection status for each user. Provide screenshots of the user creation and the login process for both accounts.
Screenshots and Explanations
•	Command in the mongo shell creating the "aacuser" account with the "readWrite" role on the "AAC" database. 
db.createUser({ user: "aacuser",
  pwd: "YourSecurePassword",
  roles: [{ role: "readWrite", db: "AAC" }]
})
•	Confirmation output showing successful creation of the "aacuser" account.

<img width="468" alt="image" src="https://github.com/user-attachments/assets/7b254829-3a3e-49af-80a9-a09e07fb5841" />

•	Logging into MongoDB as the admin user, including the login command and the output of db.runCommand({connectionStatus:1}) showing the admin user's connection status. 

<img width="468" alt="image" src="https://github.com/user-attachments/assets/8e8cf69f-b589-4a04-882d-9cdaf6d87d0e" />

•	Logging into MongoDB as "aacuser", including the login command and the output of db.runCommand({connectionStatus:1}) showing the "aacuser" connection status. 

<img width="468" alt="image" src="https://github.com/user-attachments/assets/d5b13ff2-94f3-4e54-ac11-0bbd4e6cbe3c" />

 
Developing the Python Module for CRUD Operations: animal_shelter.py
Task:
Development Process
1.	Create Functionality:
o	Validates input to ensure it is a dictionary.
o	Inserts the document and returns confirmation of success.
o	Challenge: Handling invalid data formats. 
o	Solution: Implemented validation with Python's isinstance() function.
Create a Document

<img width="318" alt="image" src="https://github.com/user-attachments/assets/a2f60a7c-2334-474c-b0cf-9eb78296c14c" />

 
Output Screenshot

<img width="468" alt="image" src="https://github.com/user-attachments/assets/a1c6576d-37a8-4d7c-b143-0aeb75936f92" />

 
2.	Read Functionality:
o	Accepts a query parameter and retrieves matching documents.
o	Formats the output using json.dumps() for better readability.
o	Challenge: Managing empty queries. 
o	Solution: Returns an empty list and a message if no matches are found.
Query a Document

<img width="468" alt="image" src="https://github.com/user-attachments/assets/ff975cf0-7c64-4774-a358-bdc2c55891c4" />

Output Screenshot

<img width="468" alt="image" src="https://github.com/user-attachments/assets/6e6453bf-bac8-41d2-8d1f-923f3dc2d651" />

 

4.	 Update Functionality
o	Filters documents based on the query (e.g., animal_id).
o	Modifies only the specified fields without affecting other data.
o	Challenge: Preventing accidental updates to multiple documents.
o	Solution: Used update_one for targeted updates.
Update a Document

<img width="468" alt="image" src="https://github.com/user-attachments/assets/8d0cb791-75b2-4bec-a7fb-4e36a39ec1fd" />

Output Screenshot 

<img width="468" alt="image" src="https://github.com/user-attachments/assets/9607c652-59ff-4880-830b-e224a5eb9bc7" />


6.	Delete Functionality
o	Filters documents based on the query (e.g., animal_id).
o	Removes only the documents that match the criteria.
o	Challenge: Ensuring correct deletion of intended documents.
o	Solution: Returned the count of deleted documents for verification.
Delete a Document

<img width="468" alt="image" src="https://github.com/user-attachments/assets/54ab1a30-8105-425d-8b01-28c9acd01bbb" />

Output Screenshot

<img width="468" alt="image" src="https://github.com/user-attachments/assets/42ea4656-2104-4601-88e1-c1d080aea67e" />


 
MongoDB Data Modifications
Rationale for Terminal-Based Updates:
To avoid saturating the Python code with additional complexity, rescue type modifications were handled directly in MongoDB through the terminal. This approach ensures the codebase remains modular and clean, focusing on CRUD operations without overburdening it with preprocessing logic. By leveraging MongoDB\u2019s flexibility, rescue types were efficiently updated using bulk commands, which also improved runtime performance by precomputing data.

<img width="428" alt="image" src="https://github.com/user-attachments/assets/c08c0a38-7c64-4820-8e79-cb8e0d4ed087" />

 
 
Dashboard Implementation.
1. Importing Necessary Modules
   
   <img width="228" alt="image" src="https://github.com/user-attachments/assets/0e77da48-48f8-4b68-8059-ad0aff583ecb" />

 
Explanation:
•	JupyterDash: A variant of the Dash framework that lets you run Dash apps in Jupyter notebooks.
•	dash_leaflet: Dash component library for rendering interactive maps using Leaflet.js.
•	dash, dcc, html: Core libraries from Dash to create web-based interactive components (Dropdowns, Graphs, HTML layout elements).
•	plotly.express: A high-level plotting library to quickly create charts such as pie charts, bar plots, etc.
•	dash_table: Allows creation of interactive data tables.
•	dash.dependencies: Used to declare callback inputs/outputs for responsive, data-driven interactions.
•	base64: Used to encode images (like logos) as Base64 strings for embedding in the Dash app.
•	pandas, numpy: Standard data manipulation libraries in Python.
•	animal_shelter: Custom module containing the AnimalShelter class, which is presumably a wrapper to interface with a MongoDB database.

2. Data Manipulation / Model

<img width="432" alt="image" src="https://github.com/user-attachments/assets/9d1fcd4f-8208-4607-8dfa-a0be22663e04" />

 Explanation:
1.	shelter = AnimalShelter()
Initializes an instance of the AnimalShelter class to communicate with the MongoDB database.
2.	df = pd.DataFrame.from_records(shelter.read({}))
o	Calls shelter.read({}) to query all records from the database and converts them into a pandas DataFrame.
3.	Removing _id column
o	MongoDB documents typically have an _id field. The code drops it for cleanliness or to avoid serialization issues in Dash.
4.	Flattening rescue_type
o	Some records may store rescue_type as a list. The lambda function joins list elements with commas if rescue_type is a list.
5.	RESCUE_TYPE_MAP
o	A dictionary that categorizes certain breeds under specific rescue types. It helps in grouping the data or validating data entries.

3. Creating the Dash App and Embedding a Logo

<img width="432" alt="image" src="https://github.com/user-attachments/assets/d0b941f2-dd50-43a8-93b0-9a603922e772" />

 Explanation:
1.	JupyterDash app initialization
o	app = JupyterDash(__name__) sets up a Dash app that can be run in a Jupyter Notebook or standalone.
2.	Loading and embedding an image
o	The logo (e.g., “Grazioso Salvare Logo.png”) is opened in binary mode, encoded in Base64, and stored in encoded_image.
o	The src attribute of html.Img is set to the Base64 string so the image can be displayed directly by the browser.
3.	App layout
o	Uses Dash’s HTML components to build the page structure:
	A hidden div used for possible storing of data or callback triggers.
	A centered header with SNHU and user identifier.
	A clickable logo linking to SNHU’s website.
	A Dropdown (dcc.Dropdown) that lets the user filter data by rescue type.
4. Creating a Data Table and Pie Chart


<img width="432" alt="image" src="https://github.com/user-attachments/assets/cef52160-6030-42fc-87a5-a6aa86c62a9a" />

 Explanation:
1.	DataTable
o	Displays the queried animal data in a tabular format.
o	columns are generated dynamically based on df.columns.
o	Each row is selectable (row_selectable='single'), so the user can click a row and see details elsewhere.
o	sort_action and filter_action both set to 'native', allowing sorting and filtering directly on the client side.
o	selected_rows=[0] automatically selects the first row upon page load.
2.	Layout for map and pie chart
o	After the table, a Div labeled map-id is placed to hold the interactive Leaflet map.
o	Another Div contains a dcc.Graph for displaying a pie chart. Both are placed side by side using Flexbox styling.

5. Callbacks for Filtering Data and Updating the Pie Chart
   
   <img width="432" alt="image" src="https://github.com/user-attachments/assets/fd8028b8-675e-4d49-9485-0a8f8e29e0d2" />

 Explanation:
1.	First callback (filter_data):
o	Triggered by: The value of the dropdown filter-rescue-type.
o	Output: Updates the data property of the DataTable (datatable-id).
o	If the user chooses a specific rescue type (e.g., “Water Rescue”), it filters the DataFrame to show only rows matching that rescue type. If “Reset” is chosen, it shows all rows.
2.	Second callback (update_pie_chart):
o	Triggered by: The same dropdown filter-rescue-type.
o	Output: Updates the figure of the pie chart (pie-chart).
o	Logic: Filter the DataFrame similarly. Then compute how many animals belong to each breed, limit to the top 10, combine any remaining breeds into an “Other” category, and finally create a pie chart with Plotly Express.

6. Callback to Update the Map
   
   <img width="432" alt="image" src="https://github.com/user-attachments/assets/4401bf4b-b95e-4e50-a370-26b0b164bafa" />

 Explanation:
•	Callback is triggered whenever the data in the table changes or a different row is selected.
•	Checks if any row is selected (derived_virtual_selected_rows). If nothing is selected, returns a default map centered at [0, 0] with zoom level 1.
•	Otherwise, extracts the latitude (location_lat) and longitude (location_long) from the selected row and updates the map to center on that location.
•	dl.TileLayer(): The base map layer from Leaflet.
•	dl.Marker(): A pin dropped at the location. Contains a Tooltip (showing breed) and a Popup (showing the animal’s name).

8. Running the Server
   
   <img width="156" alt="image" src="https://github.com/user-attachments/assets/5347f0fb-37f2-462b-af2c-3b8fc7aadd0d" />

 
Explanation:
•	app.run_server(debug=True) starts the local server in “debug” mode, providing detailed error messages and live reloading if changes are made to the code.
•	Once running, you can view the dashboard by navigating to the provided local web address (usually http://127.0.0.1:8050 or similar).

Screenshots of the finished Dashboard:
    <img width="432" alt="image" src="https://github.com/user-attachments/assets/d30c891e-951e-4d6b-a2f6-6f6345fbd6fa" />
    <img width="432" alt="image" src="https://github.com/user-attachments/assets/11cff6c2-e958-44ae-b15b-e1c381c9ffbb" />
    <img width="432" alt="image" src="https://github.com/user-attachments/assets/5260c355-f747-49ac-a2f0-9ba524269102" />
    <img width="432" alt="image" src="https://github.com/user-attachments/assets/b599f336-401b-4936-8f9e-dcf65064b3b3" />




