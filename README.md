         `/////        .-`        :////. /:    `/-                                 -/`              
        +sohMMMo/     -MMN/     :oooMMMhoMh   osMs                               `ohM:              
      /h/: ./mMMNh:    ..ho   .ho/``:sMMMMh +hMMMs                              yhMMM:  -hhh`       
    -mNM.    .-MMM/    -++   dmMo    `..... `.NMMs     `sdmmm+`      .dddmm`:m/ .:MMM: `/MMM`       
    -MMM.      MMM/    `     mMMo             mMMs   .oM/ dmMMM:. `.dN`  smMMM+  .MMM/:NMMo-        
    -MMM.      MMM/          mMMo             mMMs  `MMM/  -ymMMm +MMN     yyy:  .MMMMMhdMMM/:      
    -MMM.      MMM/          mMMo             mMMs  `MMM/    sMMm +MMN           .MMMyo .omMMd      
    -MMMhs     Md/.          mMMmy.      yo   mMMs  `MMMdy   sMMm +MMMy+         .MMM:    yMMd      
    `-yMMMdo yd-.            ./MMMmd`  sd-.   mMMNd- -oMMMmy sM:. `-dMMNd:  -d/  .MMMmh   yMMNd/    
       `hmmmm:`                `+mmmmmm/`     hmmo`    `smmmm+`      .mmmmmmy`   .mmm:`   smmy`   
----------------------------------------------------------------------------------------------------
# mormon

Pen. Testing Tool Made w/ Python

## Getting Started

Run the program using the "run.bat" file. To change the parameters please edit the "config.xml" file. You will need the prerequisites listed below.

### Prerequisites

You will need:
*Python 3.5
*The Python modules: Beautiful Soup and Requests

It may be benificial to use "pip" when installing these modules.

## Config Usage

```
<mormon>
	<password>changeme</password> 	#Password to Check
	<start>067700000</start>	    #Number to start at
	<end>500</end>			        #Length of search
	<mark>100</mark>		        #Mark progress every X login attemps
	<startdelay>0</startdelay>	    #Delay for Y seconds after startup
	<delay>0</delay>		        #Delay in between chunksets
	<chunkset>10<chunkset>		    #Check X usernames before resting for Y seconds of time
</mormon>
```

## Built With

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/en/master/)

## Authors

* **Ben Weisz** - *Programmer* - [BenceW](https://github.com/BenceW)
* **Emil Ilnicki** - *Exploit Locator* - [No Profile]()
* **Klarence Estepa** - *Programmer/Social Engineering* - [thehappyturtle](https://github.com/thehappyturtle)
* **Rajvir Samrai** - *Programmer* - [stone-4](https://github.com/stone-4)

## License

This project is licensed under the MPL 2.0 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Mr. Kolch
* D2L DPCDSB
* Morman Jesus
