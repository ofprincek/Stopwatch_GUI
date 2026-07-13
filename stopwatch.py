import time
import threading


def time_format(seconds):
    ms=int((seconds%1)*1000)
    s=int(seconds)
    h=s//3600
    m=(s%3600)//60
    s=s%60
    return f"{h:02d}:{m:02d}:{s:02d}:{ms}"


def stopwatch():
    start=time.time()
    total_time=0
    running=True
    running_timer=True
    paused_timer=False    # shoutout to GPT for this
    
    
    
    def timer():
        while running_timer:
            if not paused_timer :   # if(paused==False):
                elapsed=time.time()-start+total_time
                print(f"\r    {time_format(elapsed):<20}", end=" ", flush=True)
                time.sleep(0.05)
    
    
    print("Stopwatch is running.. enter p to pause OR enter s to stop")
    
    display=threading.Thread(target=timer)
    display.start()
    
    
    while running:
        
        command=input("").lower()
        
        if command=="s" :
            end=time.time()
            running_timer=False
            display.join()
            total_time+=end-start
            print(f"Total Time: {time_format(total_time)}")
            run=input("run again? y/n:\n").lower()
            if run!="y" :
                print("see u again.")
                running=False
                return False
            else:
                return True
            
        elif command =="p" :
            pause=time.time()
            paused_timer=True
            total_time+=pause-start
            print(f"Current Total Time: {time_format(total_time)}")
            if input("resume? y/n:\n").lower()=="y":
                start=time.time()
                paused_timer=False
                print("Stopwatch is running.. enter p to pause OR enter s to stop")
            else:
                running_timer=False
                display.join()
                return False
            
        else:
            print("invalid input. please try again.")
                      
        
def main():
    run=True
    while run:
        run=stopwatch()
    print("no worries, see u again!")
    

if input(">> run stopwatch? y/n\n").lower()=="y" :
    main() 
else: 
    print("no worries, see u again!")
    
    