from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def info(bot, update):
    msg = 'FiglioDiUnPandaBot\n\n' + 'Allora... adesso mi descrivo un pochino... aspetta solo un secondo e sono da te... spetta spetta...\n'
    msg += 'Praticamente sono me stesso, su questo credo di essere sicuro, ma se considero che questa cosa è così allora no... spetta spetto...\n'
    msg += 'No, per me è no. Grazie lo stesso. Di sto cazzo, ma grazie che... ODDIIIOOOO! Un panda, che schifo quegli animali... aspetta, ma io...\n'
    msg += 'Fanculo a tutti, mi fate solo confondere! Sciò!!!\n\n' + 'La lista dei comandi ve la do però, se no poi chi la sente a quella...\n'
    msg += '/saggimezza: Beh, sono io che dico cose\n'
    msg += '/diamoinumeri: Numeri Ad minchiam\n'
    msg += '/oroscopo: Per conoscere il tuo futuro'
    update.message.reply_text(msg)

def start(bot, update):
    update.message.reply_text('Incredibile, anche un pirla come te sa parlare!')

def oroscopo(bot, update):
    update.message.reply_text(
        'Siamo nel 2017, {} fatti inculare da un Panda superdotato!'.format(update.message.from_user.first_name))

def saggimezza(bot, update):
    frasi = ["Oggi sono andato al mare ma i criceti gialli hanno detto che " +
            "li hanno finiti tutti, eppure io li avevo prenotati da almeno qualche minuto...",
            "Ieri era la giornata dedicata alle oche e quindi ho deciso di " +
            "salvare il mondo sfamando i piccioni della Normandia...",
            "33 trentini andarono a Trento perché la loro casa era lì, ma la " +
            "mia non ricordo più in quale oleodotto messicano l'ho lasciata...",
            "Se le foche fossero delle così brave persone come si dice non " +
            "fumerebbero i sigari al contrario come fanno le femmine delle nutrie...",
            "Le alici asiatiche sono le migliori senza ombra di dubbio, infatti " +
            "quando vado in montagna il calzolaio me lo dice semple...",
            "I mitocondri primordiali non sono più come quelli di una volta, " +
            "prendono le valigie e partono per la cucina...",
            "L'acido desossiribonucleico è stato al mare solamente una volta, " +
            "ha incominciato a respirare meglio ma la montagna è meglio...",
            "Se non si è sicuri di quello che si fa la valigia la si dimentica " +
            "in aeroporto come qualche anno fa alle Maldive...",
            "La cannabis è una pianta diversa dalle altre e le orchidee sono " +
            "magnifiche betulle come narrano le leggende, almeno mi sembra...",
            "Dai miei anni di esperienza ti posso solo dire che gli sconosciuti " +
            "non li puoi conoscere mai abbastanza, nonostante siano criceti...",
            "Meglio un giorno da leoni senza mutande che la scuola a settembre " +
            "senza i professori che maturano le avversità dell'annata...",
            "Quando la gente prova ad offenderti senza apparente motivo in realtà " +
            "la terra volge al calar dell'alba sulle tue membra...",
            "Non è essere cattivi Panda prendere a sberle le perle delle signore " +
            "che si atteggiano da monarche benestanti dell'est...",
            "La scena del crimine era stata segnata da quei pinguini malandrini " +
            "in fila per entrare in quella discoteca senza carta igienica...",
            "Le piattole sono comode per servire le pietanze dei giganti, ricche " +
            "di nutrienti e piedini insaporiti dal sapore della vita...",
            "Le ventole a cui sono sottoposte le zebre sono particolarmente " +
            "rumorose per la quantità di denari con cui le hanno costruite...",
            "Un inglese e un francese entrano in un bar e ad un certo punto un " +
            "tedesco entra e grida: \"Pandaaa!\", al che mi spavento...",
            "Gli applausi non erano rivolti a lei come tutti pensavano, bensì a " +
            "quel passero nascosto nella penombra che pensava alla morte...",
            "Le scatole vuote sono utensili necessari per i gatti conquistatori " +
            "del cosmo più inesplorato dell'intero mondo emerso delle montagne...",
            "Quando si vuole stare soli è possibile isolarsi in Cassiopea, dea delle " +
            "annate misteriose del Naair, ultimo membro degli Zaar...",
            "È inevitabile e potente, possente quando succube delle vie nascoste. " +
            "Siano noi o siete voi? La risposta è dentro tutti...",
            "Gli stivali non hanno un senso proprio. Sottoposti alla luce terrena " +
            "inaspriscono le onde più profonde e si propagano senza meta...",
            "Il cosmo e i suoi misteri rendono un Panda perplesso e meravigliato. " +
            "Le patatine lo riportano alla realtà, tutti lo sapevano...",
            "Un panda su due zampe è capace di creare ciò che un cavallo a 4 zampe " +
            "non potrebbe nemmeno immaginare con il pensiero...",
            "Tutti odiamo le siepi d'inverno, mai che ti abbraccino e ti consolino, " +
            "come se tu gli avessi fatto un torto persoanale, però ai piccioni sì!...",
            "Le voragini del celo sono vicine, l'ozono è sceso sulla terra per liberare " +
            "le catene dell'animo viscerale delle ulcere inguinali, sarà la fine?...",
            "Non è necessario essere scaltri per vedere col tatto, e altrettanto " +
            "lontane sono le montagne del futuro che permettono la salvezza eterna...",
            "Le saracinesche ci nascondono verità a noi nascoste senza poterle vedere, " +
            ", siamo vittime inconsce di quello che vogliono farci credere, scappate...",
            "Le urla non si sentivano da così tanto lontano, allora mi avvicinai e le " +
            "sentii sempre più forti, ad un certo punto smisero, ma forse ero io...",
            "In futuro ci saranno persone che andando in vacanza cadranno nel peccato " +
            "mortale di lavorare con onore e disprezzo..."]
    estrazione = random.randint(0, 29)
    update.message.reply_text(frasi[estrazione])

def diamoinumeri(bot, update):
    update.message.reply_text('Non sono cazzi miei quello che ci fai: ' + str(random.randint(1, 1000)))

def nonDireQuello(bot, update):
    if 'panda' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="OOOh! Non osare nominarmi me medesimo!!!")
    elif 'andiamo' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Dove!? Dove!? Dove!?")
    elif 'figlio' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Parli con me? Eh!?")
    elif 'grazie' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Ma precccco!")
    elif 'cazzo' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Astinenza da fagiano?")
    elif 'coglione' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Un coglione vuole sempre un compagno con cui sparlare del boss centrale...")
    elif 'ciao' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Minchia l'originalità dei saluti...")
    elif 'notte' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Arriva il meteorologo!")
    elif 'giorno' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Arriva il meteorologo!")
    elif 'birra' in update.message.text.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Me piaaaaace...")

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ma come cazzo parli!")

updater = Updater('398156401:AAFBbBmLCgRcuxnj0H0UaesSvKHh3tl7foU')
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('oroscopo', oroscopo))
updater.dispatcher.add_handler(CommandHandler('saggimezza', saggimezza))
updater.dispatcher.add_handler(CommandHandler('diamoinumeri', diamoinumeri))
updater.dispatcher.add_handler(MessageHandler(Filters.text, nonDireQuello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, caps))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()
