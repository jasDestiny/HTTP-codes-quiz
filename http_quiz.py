import random 
from datetime import datetime

class quiz:
    def __init__(self, hashes=[], n=0):
        self.n=n
        now = datetime.now()
        self.dt=now.strftime("%d/%m/%Y %H:%M:%S")
        self.hashes=[[100, "Continue"],[101, "Switching Protocol"],[102, "Processing"],[103, "Early Hints"],
                     [200, "OK"],[201 , "Created"],[202 , "Accepted"],[203 , "Non-Authoritative Information"],[204 , "No Content"],[205 , "Reset Content"],[206 , "Partial Content"],[207  , "Multi-Status"], [208 , "Already Reported"],[226 , "IM Used"],
                     [300 , "Multiple Choices"],[301,"Moved Permanently"],[302, "Found"],[303, "See Other"], [304, "Not Modified"],[305  , "Use Proxy"],[306 , "Switch Proxy"],[307  , "Temporary Redirect"],[308  , "Permanent Redirect"],
                     [400, "Bad Request"],[401 , "Unauthorized"],[402 , "Payment Required"],[403 , "Forbidden"],[404 , "Not Found"],[405 , "Method Not Allowed"],[406 , "Not Acceptable"],[407  , "Proxy Authentication Required"], [408 , "Request Timeout"],[409, "Conflict"],[410 , "Multiple Choices"],[411,"Length Required"],[412, "Precondition Failed"],[413, "Payload Too Large"],
                     [414, "URI Too Long"],[415 , "Unsupported Media Type"],[416 , "Range Not Satisfiable"],[417 , "Expectation Failed"],[418 , "I'm a Teapot"],[421 , "Misdirected Request "],[422 , "Unprocessable Entity"],[423  , "Locked"], [424 , "Failed Dependency"],[425, "Failed Dependency"],[425 , " Too Early"],[426,"LUpgrade Required"],[428, "Precondition Required"],[429, "Too Many Requests"],[431, "Request Header Fields Too Large "],[451, "Unavailable For Legal Reasons"],
                     [500, "Internal Server Error"], [501, "Not Implemented"], [502, "Bad Gateway"], [503, "Service Unavailable"], [504, "Gateway Timeout"], [505, "HTTP Version Not Supported"], [506, "Variant Also Negotiates"], [507, "Insufficient Storage"], [508, "Loop Detected"], [510, "Not Extended"], [511, "Network Authentication Required"],
                     ["1xx", "informational response"],["2xx", "successful"] ,["3xx", "redirection"], ["4xx", "client error"] , ["5xx", "server error"]
                     ]
        if not n:
            n=len(hashes)
        self.userResponse=[]
        if hashes:
            self.hashes=hashes
        self.quizQuestions=self.getRandomQuestion(self.hashes)
        self.score=0
        self.conductQuiz()
        print("\nYour score:", self.score, "%")
    
    def conductQuiz(self):
        j=0
        for i in self.quizQuestions[:self.n]:
           print("")
           print("QN0", j+1)
           print("What does the HTTP code", i["qno"], "mean?")
           choices={}
           for k in range(0, 4, 1):
               choices[(chr(ord("a")+k))]=i["options"][k]
           for a, b in choices.items():
               print(a, ")", b)
           j+=1
           userAnswer=input("Enter answer option: ")
           while len(userAnswer)>1 or len(userAnswer)<1 or not(ord(userAnswer)>=ord("a") and ord(userAnswer)<=ord("d")):
               userAnswer=input("Enter Valid answer option: ")
           self.userResponse.append(userAnswer)
           if choices[userAnswer]==i["ans"]:
               self.score+=1
           else:
               print("Correct answer:", i["ans"])
        self.score/=self.n
        self.score*=100
    
    def storeResults(self):
        print(self.score)
        
    def printQuestions(self):
        print(self.dt)
        for i in self.quizQuestions:
            print(i)
        
    def getRandomQuestion(self, hashes):
        done=set()
        questions=[]
        i=0
        while len(questions)<len(hashes):
            r=random.randint(0, len(hashes)-1)
            if r in done:
                continue
            question={"qno":hashes[r][0], "ans":hashes[r][1]}
            options=[]
            while len(options)<4:
                options.append(hashes[random.randint(0, len(hashes)-1)][1])
            options[random.randint(0, 3)]=hashes[r][1]
            question["options"]=options
            questions.append(question) 
            done.add(r)
        return questions
q=quiz(n=int(input("Enter the number of questions: ")))

# Reverse quiz: https://niisar.gitbooks.io/cs/content/http-status-code-quiz.html