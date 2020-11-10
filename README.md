# Defining the problem 

Для закордонної поїздки вам потрiбно отримати кiлька довiдок вiд держустанови. Проте, виявилося, що для отримання цих довiдок потрiбнi iншi довiдки, а тi, в свою чергу, потребують ще iнших довiдок. 
На отримання кожної довiдки потрiбно вистояти чергу, тому ви хочете зекономити час, не стоячи в черзi дарма (якщо ви не будете мати потрiбних довiдок, стоячи в черзi, вам вiдмовлять у видачi цiєї). 
Маючи iнформацiю про те, якi довiдки потрiбнi для яких, визначте оптимальний порядок отримання усiх довiдок, при якому вам жодного разу не вiдмовлять у видачi. Якщо таких оптимальних варiантiв кiлька — виведiть будь-який iз них. 

## Input
Кожен iз N рядкiв вхiдного файлу govern .in мiстить два слова, роздiленi пробiлом — назва довiдки та довiдка, яку потрiбно отримати перед нею. 

- Рядкiв може бути вiд 1 до 100000. 
- Слова мають довжину вiд 1 до 50 лiтер i складаються з цифр 0-9 i малих лiтер латинського алфавiту вiд a до z. 
- Якщо для однiєї довiдки потрiбно отримати N iнших, файл мiститиме N рядкiв, що починатимуться на одне й те саме слово. 
- Гарантовано iснує хоча б один порядок отримання довiдок, при якому можна отримати усi довiдки. 

 Example 1:
    
        visa foreignpassport 
        visa hotel 
        visa bankstatement 
        bankstatement nationalpassport 
        hotel creditcard 
        creditcard nationalpassport 
        nationalpassport birthcertificate
        foreignpassport nationalpassport
        foreignpassport militarycertificate
        militarycertificate nationalpassport 
        
Example 2:

        visa foreignpassport


## Output 
Вихiдний файл govern .out повинен мiстити M рядкiв — назви довiдок в порядку їх рекомендованого отримання. <br>
Примiтка: Пiсля останнього слова також повинен бути символ переносу рядка (new line). 

 Example 1:
 
    birthcertificate 
    nationalpassport 
    militarycertificate 
    foreignpassport 
    creditcard 
    hotel 
    bankstatement 
    visa 
    
  Example 2:
  
    foreignpassport 
    visa 
    
 # Logic behind implementation:
 
 - Stem 1: Read the input 'govern.in' file and build a graph from it. In my case I'm using dictionary representation of adjastency matrix
 
 - Step 2: In graph that was built from input find such vetrex that all the other are reachable from it. From now and so on I'll call it a mother vertex. In case there are a couple of mother vertices choose any
 
 - Step 3: Perform a modofied dfs starting from mother vertex. Use following modification: for each vertex that the algorithm reaches recursively before appending it to the queue check if all of its ancestors have been visited before, if not move on and not append it to the queue. Return list with reversed resulting sequence 
 
 - Step 4: Write resulting sequence into output 'govern.out' file
 

