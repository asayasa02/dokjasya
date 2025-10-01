define d = Character("Dokja", color="#1B3C53")
define a = Character("[povname]", color="#d45b5b")

default povname = ""

label start:
    scene bg sekul
    show dokja happy

    d "HIII"
    d "I'm Dokja, what is your name?"
    $ povname = renpy.input("What is your name?", length=32).strip()
    d "Oouh hi [povname]!"
    d "I've always wanted to be your friend since I saw you."
    d "Can we be friend? please??"

    a "Eummm"
    
    menu:
        "Yesss we can":
            jump good

        "Nuh uh":
            jump bad   

        "Eummmm":
            jump netral  

label bad:
    show dokja upset
    d "Tch"
    d "How dare you!!"
    d "I never want to see you again"
    d "BYE"
    "Dokja left,  and you never saw him again... until you die-but you die today.."
    "What a loss"
    "BAD ENDING stupid"
    return

label good:
    scene bg sekul
    show dokja shy   
    d "awww really??"
    "You be friend with him, and he treat u so well. Goodluck"
    "GOOD ENDING"
    return

label netral:
    scene bg sekul
    show dokja freaky
    d "Hummm?"
    d "Soo?"

    jump netral1  

label netral1:
    scene bg sekul
    show dokja upset
    d "I guess u dont want to be my friend..."

    menu:
        "Actually i want to be your friend. Im just shy":
            jump good

        "Sorry i dont want to be your friend":
            jump bad

        "Actually, I like you!":
            jump marriage  

label marriage:
    show dokja freaky
    d "Really? Let's get married!!!!!!!!!!!!1"
    d "OMGGGGDYEGFWUGFWGIU3YR893YR8YFRUIHGFCUIGFHUIEGFIUERFUIGWFUIW"
    "judhfoiuerhvoirehviernvlkrevbnreihboiehbiroebherhnvlkrhiohwbir"
    "eerrrror"
    "Meaaoage eendinghs"
    "Congrstrdysd"
    return