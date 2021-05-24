# Colab-Timeout
Simple Python code to scroll periodically to prevent colab time out.

Run the python script and switch to colab tab, At regular interval screen will be scrolled up and down (by same amount) so inctivity is not detected.

NOTE 1 - You need to keep the colab tab open while running the script

NOTE 2 - You can start/stop the script whenever required, that will not affect your chrome tab



Wait Time - Time(in seconds) between two consecutive Scrolls

USAGE

Setup

    git clone https://github.com/BeKingsman/Colab-Timeout
    cd Colab-Timeout
    pip install -r requirements.txt
    
    
Execute Script

        python main.py       // Default Wait Time will be 30 seconds
        
        OR
        
        python main.py 100   // Wait Time will be 100 seconds
        
  

