from tkinter import * 
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

# Create an SQLAlchemy engine
# engine = create_engine("mysql+mysqlconnector://root:SQLPassword12#@localhost/itvedant")

# # Read data using SQLAlchemy
# query = "SELECT * FROM leaderboard"
# self.data = pd.read_sql(query, engine)




class Dashboard():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800")
        self.root.title("Leadership Dashboard")
        self.root.configure(bg="#0d0d1a")
        
        # Sample data (replace with MySQL data fetch logic)
        # self.data = pd.DataFrame({
        #        'Name': ['Simmy Maurya', 'Diksha Kumari', 'Priyanshu Bisht', 'Kritika Rahi', 'Akshay Gupta','Prince Saini','Rakesh Dangwal','Rashmi','Harsh','Riya Rawat'],
        #     'Attendance': [8.71, 8.24, 9.33, 10, 9.14,9.11,9.68,8.94,9.34,9.23],
        #      'Assignment': [18.22, 18.06, 18.67, 19.15, 18.42,19,17.21,19.03,14.55,19],
        #      'Assessment': [14.17, 13.83, 12, 10.23, 9.37,15,8.17,3.69,8.26,16],
        #      'Internal_Mock': [20, 20, 30, 40, 40,50,40,50,45,65],
        #      'Project_Evaluation': [30, 50, 70, 60, 50,50,75,65,34,84],
        #      'CCE_Exam': [20, 30, 10, 30, 40,60,20,75,64,34]})
        engine = create_engine("mysql+mysqlconnector://root:SQLPassword12#@localhost/itvedant")
        query = "SELECT * FROM leaderboard"
        self.data = pd.read_sql(query, engine)
        # conn = mysql.connector.connect(host="localhost",user="root",password="SQLPassword12#",database="itvedant")
        # query = "SELECT * FROM leaderboard"
        # self.data = pd.read_sql(query, conn)
        # conn.close()
        
        self.data['Score'] = self.data.iloc[:, 2:].sum(axis=1)

        # Machine Learning - Linear Regression
        self.X = self.data[['attendance', 'assignment', 'assessment', 'internal_mock', 'project_evaluation', 'cce_exam']]
        self.y = self.data['Score']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

        # Slicer Dropdown
        self.selected_student =StringVar()
        self.selected_student.set('All Students')
        Label(root,text="Class Status",font=('Arial', 20, 'bold'),fg='white',bg='#0d0d1a').pack(side='top')
        slicer_frame = Frame(root)
        slicer_frame.place(x=550,y=350)

        Label(slicer_frame, text='Select Student:').pack(side='left', padx=10)
        slicer = ttk.Combobox(slicer_frame, textvariable=self.selected_student, values=['All Students'] + list(self.data['name']))
        slicer.pack(side='left', padx=10)
        slicer.bind('<<ComboboxSelected>>', lambda e: self.update_charts())

        # KPI Section
        self.kpi_frame = Frame(self.root,bg="#0d0d1a")
        self.kpi_frame.place(x=580,y=450)

        self.kpi_frame2 = Frame(self.root,bg="#0d0d1a")
        self.kpi_frame2.place(x=600,y=550)

        self.avg_score = np.mean(self.data['Score'])
        self.top_score = np.max(self.data['Score'])
        
        Label(self.kpi_frame, text=f'Average Score: \n{self.avg_score:.0f}', font=('Arial', 16, 'bold'),fg='white',bg='#0d0d1a').pack(side='left', padx=20)
        Label(self.kpi_frame2, text=f'Top Score: \n{self.top_score:.0f}', font=('Arial',16, 'bold'),fg='white',bg='#0d0d1a').pack(side='left', padx=20)

        # Calculate top scorer's name
        self.top_scorer = self.data.loc[self.data['Score'].idxmax()]['name']

        # Display Top Scorer's Name
        self.kpi_frame3 = Frame(self.root, bg="#0d0d1a")  # Match background color
        self.kpi_frame3.place(x=580, y=150)

        Label(self.kpi_frame3,text=f'Top Scorer: \n{self.top_scorer}',font=('Arial', 16, 'bold'),fg='white',bg='#0d0d1a').pack(side='left', padx=20)
        Label(self.kpi_frame, text=f'Average Score: \n{self.avg_score:.0f}', font=('Arial', 16, 'bold'), fg='white', bg='#0d0d1a').pack(side='left', padx=20)

        # Get Top 5 records by Score
        self.top_5_data = self.data.nlargest(5, 'Score')

        # Visualization - Bar Chart for Top 5 Scores
        self.bar_chart_frame = Frame(self.root, width=400, height=300, bg="#0d0d1a",highlightbackground="white",highlightthickness=2)
        self.bar_chart_frame.place(x=40, y=25)

        fig, ax = plt.subplots(figsize=(5, 3))
        fig.patch.set_facecolor('#0d0d1a')
        ax.set_facecolor('#0d0d1a')
        # Plot bar chart
        bars = ax.bar(self.top_5_data['name'], self.top_5_data['Score'], color='skyblue')
        # Remove Y-axis for clean look
        ax.yaxis.set_visible(False)

        # Add scores on top of bars
        for bar, score in zip(bars, self.top_5_data['Score']):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3,f'{score:.0f}', ha='center', color='white', fontsize=10)

        # Rotate names with padding
        plt.xticks(rotation=45, ha='right', fontsize=10, color='white')

        # Adjust layout to prevent cutting names
        plt.subplots_adjust(bottom=0.3)

        # Title and styles
        ax.set_title('Top 5 Scores', color='white', fontsize=12)
        ax.spines['bottom'].set_color('white')
        ax.tick_params(colors='white')

        # Embed chart into Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.bar_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Visualization - Pie Chart
        self.pie_chart_frame = Frame(root,bg='#0d0d1a',highlightbackground="white",highlightthickness=2)
        self.pie_chart_frame.place(x=800,y=30)
        self.fig_pie, self.ax_pie = plt.subplots(figsize=(5, 3))
        self.fig_pie.patch.set_facecolor('#0d0d1a')  # Background color of the plot
        self.ax_pie.set_facecolor('#0d0d1a') 
        self.scores_by_category = self.data.iloc[:, 2:8].sum()
        self.ax_pie.pie(self.scores_by_category, labels=self.scores_by_category.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors,textprops={'color': 'white'} )
        self.ax_pie.set_title('Score Distribution by Category',color='white')
        self.canvas_pie = FigureCanvasTkAgg(self.fig_pie, master=self.pie_chart_frame)
        self.canvas_pie.draw()
        self.canvas_pie.get_tk_widget().pack()

        # Visualization - Stacked Bar Chart
        self.stack_chart_frame =Frame(root,bg='#0d0d1a',highlightbackground="white",highlightthickness=2)
        self.stack_chart_frame.place(x=40,y=390)
        self.fig_stack, self.ax_stack = plt.subplots(figsize=(5, 3))
        self.fig_stack.patch.set_facecolor('#0d0d1a')  # Background color of the plot
        self.ax_stack.set_facecolor('#0d0d1a')
        self.data.set_index('name').iloc[:, :6].plot(kind='bar', stacked=True, ax=self.ax_stack, colormap='tab20',)
        plt.subplots_adjust(bottom=0.4)
        self.ax_stack.set_title('Stacked Bar Chart - Score Breakdown',color='white')
        self.ax_stack.tick_params(axis='x', colors='white')
        self.ax_stack.tick_params(axis='y', colors='white')
        self.canvas_stack = FigureCanvasTkAgg(self.fig_stack, master=self.stack_chart_frame)
        self.canvas_stack.draw()
        self.canvas_stack.get_tk_widget().pack()


        self.trend_chart_frame = Frame(root,bg='#0d0d1a',highlightbackground="white",highlightthickness=2)
        self.trend_chart_frame.place(x=800,y=390)
        self.fig_trend, self.ax_trend = plt.subplots(figsize=(5, 3))
        self.fig_trend.patch.set_facecolor('#0d0d1a')  # Background color of the plot
        self.ax_trend.set_facecolor('#0d0d1a')
        self.canvas_trend = FigureCanvasTkAgg(self.fig_trend, master=self.trend_chart_frame)
        self.canvas_trend.draw()
        self.canvas_trend.get_tk_widget().pack()
        self.plot_future_trend()
        
    # def fetch_leaderboard_data(self):
        
    #     return self.data

    def plot_future_trend(self):
        self.future_scores = self.model.predict(self.X)

        # Adding a hypothetical future data point to extend the trend
        self.future_names = list(self.data['name']) + [""]
        # self.future_names = list(self.data['Name'].astype(str)) + ["Future Prediction"]

        self.future_scores_extended = np.append(self.future_scores, self.future_scores[-1] + 10)  # Extending trend
        self.ax_trend.clear()
        self.ax_trend.plot(self.future_names, self.future_scores_extended, marker='o', linestyle='-', color='deepskyblue')

        # Highlight last point
        self.ax_trend.scatter(self.future_names[-1], self.future_scores_extended[-1], color='red', zorder=3, label="Prediction")
        self.ax_trend.set_title('Future Score Trend', color='white')
        self.ax_trend.set_xlabel('Student Name', color='white')
        # self.ax_trend.set_ylabel('Predicted Score', color='white') 
        self.ax_trend.spines['bottom'].set_color('white')
        self.ax_trend.spines['left'].set_color('white')
        self.ax_trend.tick_params(colors='white')
        plt.xticks(rotation=45, ha='right', fontsize=9, color='white')
        plt.subplots_adjust(bottom=0.3)
        self.canvas_trend.draw()
        
    def update_charts(self):
        self.student = self.selected_student.get()
        self.filtered_data = self.data if self.student == 'All Students' else self.data[self.data['name'] == self.student]
    
        # # Update Bar Chart
        # ax.clear()
        # filtered_data.plot(x='Name', y='Score', kind='bar', ax=ax, color='skyblue')
        # canvas.draw()
    
        # Update Pie Chart
        self.ax_pie.clear()
        self.scores_by_category = self.filtered_data.iloc[:, 2:8].sum()
        self.ax_pie.pie(self.scores_by_category, labels=self.scores_by_category.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors,textprops={'color': 'white'})
        self.ax_pie.set_title('Score Distribution by Category',color='white')
        self.canvas_pie.draw()
    
        # Update Stacked Bar Chart
        self.ax_stack.clear()
        self.filtered_data.set_index('name').iloc[:, :6].plot(kind='bar', stacked=True, ax=self.ax_stack, colormap='tab20')
        self.ax_stack.set_title('Stacked Bar Chart - Score Breakdown',color='white')
        self.canvas_stack.draw()
    

            



if __name__=="__main__":
    root=Tk()
    obj2=Dashboard(root)
    root.mainloop()