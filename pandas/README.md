# pandas
## Lecture
Study "[Solving real world data science tasks with Python Pandas!](https://www.youtube.com/watch?v=eMOA1pPVUc4)" by Keith Galli.
(Students already had an introduction to pandas by Andreas Weiler.)

Please note:
- There's a table of contents in the description, e.g. to [skip the intro](https://www.youtube.com/watch?v=eMOA1pPVUc4&t=82s).
  Click "SHOW MORE" underneath the video.
- Activate the subtitles
- You can display the video at higher speed (Settings>Playback speed).

### Tasks
- While watching the video, work along with the instructor. Make note when something surprpises you,
  when you can think of a better solution, when you have questions: Right-click on the video timeline ("Copy video URL at current time")
  and save the link together with your comment/question.

## Lab Work
Practice further data handling, visualizations using [data from the video lecture](https://github.com/KeithGalli/Pandas-Data-Science-Tasks).

### Data Acquisition
- Make the project directory on your own computer: `mkdir <my_datavis_project_directory>`
- Change into the directory: `cd <my_datavis_project_directory>`
- Clone the repository from the above video lecture: `git clone https://github.com/KeithGalli/Pandas-Data-Science-Tasks.git`

### Data Handling and Visualization
- Change into the directory containing the sales data: `cd SalesAnalysis/Sales_Data`
- Start Jupyter Notebook: `jupyter notebook`

### Tasks
#### 'Or' in the field 'Order Date'
[Video Section](https://youtu.be/eMOA1pPVUc4?t=1311)
- What might be going on here?

#### Lambda within apply
[Video Section](https://youtu.be/eMOA1pPVUc4?t=2386)
- How can you simplify Keith's solution?

#### Adding State to the City
[Video Section](https://youtu.be/eMOA1pPVUc4?t=2503)
- Unify the two functions into one (why?)

### Incorrect x-Axis Tick Labels
[Video Section](https://youtu.be/eMOA1pPVUc4?t=2980)
- Can you find a simpler solution?

### Total Orders Per Hour
[Video Section](https://youtu.be/eMOA1pPVUc4?t=3137)
- Create the chart for two cities of your choice
  - How do you create a list of all cities?
  - How do you create the plot for a particular city?

### Avoiding 'SettingWithCopyWarning'
[Video Section](https://youtu.be/eMOA1pPVUc4?t=4047)
- Can you find a way to avoid this warning?

### Find Pairs of Products Bought Together
[Video Section](https://youtu.be/eMOA1pPVUc4?t=4314)
- What could go wrong with Keith's approach?
- How could the problem be circumvented?

### Correlation Between Product Price and Quantity Ordered
[Video Section](https://youtu.be/eMOA1pPVUc4?t=5064)
Thanks to the plot Keith finds a negative correlation between product price and quantity ordered.
- Can you find a way to quantify this correlation?
