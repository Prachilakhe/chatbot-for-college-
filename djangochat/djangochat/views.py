from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import pandas as pd
from matplotlib import pyplot as plt
import wikipedia
import webbrowser
import pandas as pd

f1 = pd.read_csv('Internship1data.csv')
f2 = pd.read_csv('placements1data.csv')

# Create your views here.
def home(request):
    return render(request,'bothome.html')

def chatI(request):
    return render(request, "chatbot.html")


def about(request):
    return render(request,"about.html")



def greet(request):
    user_name = request.GET.get('nameinput')   
    bot_response = "Hi {$user_name} how can I help you"
    return JsonResponse({'response':bot_response})



def chatbot(request):  
      user_message = request.GET.get('message')
      bot_response = process_user_message(user_message)
    #   if (bot_response == 0):
      return JsonResponse({'response':bot_response})
    #   else:
    #     return  JsonResponse({'response':"sorry I am not able to answer"})  
      

def process_user_message(query):
     
     
     if 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        
     elif 'shree' in query: 
            query = query.replace("shree","")
            results = wikipedia.summary(query, sentences=2)
            return(results)
        
     elif 'hey' in query:  
         return ("Hi how can I help you") 
     
     elif 'Tell me about it department' in query:         
         return("Department of Information Technology is established in 2002-03 with an intake of  60 to impart quality education in IT with stated vision and mission. Gradually that intake has been increased to 180.  The department is accredited by NBA.")
     
     elif 'Who is hod of it department' in query:
         return("Prof. Phutane sir is HOD of IT department ")
    
     
     elif 'Oncampus placements for last Four years' in query:
          df = pd.read_csv('placements1data.csv')
          x = df['placements']
          y = df['oncampus']
          plt.bar(x, y, color="#0077ff",width=0.8)
          plt.title('Oncampus placements')
          plt.xlabel('year')
          plt.ylabel('Number of students')
          plt.show() 
          return("done") 
     
     elif 'What is Average Package of IT department?' in query:
         return("5.29LPA")
        
     elif 'How many students got selected On campus in 2021-22' in query:
         return("113")
     
     elif 'Offcampus placements for last Four years' in query:
          df = pd.read_csv('placements1data.csv')
          x = df['placements']
          y = df['offcampus']
          plt.bar(x, y, color="#0077ff",width=0.8)
          plt.title('Offcampus placements')
          plt.xlabel('year')
          plt.ylabel('Number of students')
          plt.show() 
          return("done")
     
     elif 'how many students went for higher studies in 2020-21' in query:
         return("3")
     
     elif 'which companies recruits maximum students?' in query:
         return("companies like infosys, HCL and wipro are our mass recruiters")
     
     elif 'how many companies visited in last four years?' in query:
         return("nearly 120 to 130 companies per year")
     
     elif 'Comparison of students from last 4 years on the bases of there placements' in query:
         df = pd.read_csv("placements1data.csv")
         df.plot()
         plt.show()
         return("Done")
     
     elif 'students of it selected for Internship in 2021-22' in query:
         df=pd.read_csv('internship1data.csv')
         x=df['AY']
         y=df['2021-22']
         plt.xlabel('Acedemic Year')
         plt.ylabel('No. of students')
         plt.title("Internship in 2021-22 of IT Branch")
         plt.scatter(x,y)
         plt.show()
         return("Done")
     
     elif 'Draw pie chart for Placement data of last four years' in query:
         df=pd.read_csv('placements1data.csv')
        #  x=df['placements']
         labels=['oncampus','offcampus','higherstudies','Entrepreneur']
         y=[df['oncampus'].sum(),df['offcampus'].sum(),df['higherstudies'].sum(),df['Entrepreneur'].sum()]
         plt.axis("equal")
         plt.pie(y, labels=labels, autopct='%1.1f%%')
         plt.legend(loc='lower right')
         plt.show()
         return("Done")
     
     elif 'Draw pie chart for Internship data of last four years' in query:
         df=pd.read_csv('internship1data.csv')
        #  x=df['AY']
         labels=['2018-19','2019-20','2020-21','2021-22']
         y=[df['2018-19'].sum(),df['2019-20'].sum(),df['2020-21'].sum(),df['2021-22'].sum()]
         plt.axis("equal")
         plt.pie(y, labels=labels, autopct='%1.1f%%')
         plt.legend(loc='lower right')
         plt.title('Internship data ALL AY')
         plt.show()
         return("Done")
     
     elif 'students selected for internship in 2018-19' in query:
         df=pd.read_csv('internship1data.csv')
         x=df['AY']
         y=df['2018-19']
         plt.xlabel('Acedemic Year')
         plt.ylabel('No. of students')
         plt.title("Internship in 2018-19 of IT Branch")
         plt.scatter(x,y)
         plt.show()
         return("Done")
     
     elif 'How many copyrights done in last three years' in query:
         df=pd.read_csv('Patent_copywrite_data.csv')
         x=df['Year']
         y=df['Number of copywrites']
         plt.xlabel('Acedemic Year')
         plt.ylabel('No. of copywrites')
         plt.title("no. of copywrites ")
         plt.bar(x,y)
         plt.show()
         return("Done")
     
     elif 'How many Patents done in last three years' in query:
         df=pd.read_csv('Patent_copywrite_data.csv')
         x=df['Year']
         y=df['Number of Patents']
         plt.xlabel('Acedemic Year')
         plt.ylabel('No. of Patents')
         plt.title("no. of Patents ")
         plt.bar(x,y)
         plt.show()
         return("Done")
     
     
     