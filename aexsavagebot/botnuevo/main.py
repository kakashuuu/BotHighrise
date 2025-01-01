import random
import os
import importlib.util
from highrise import *
from highrise import BaseBot, Position
from highrise.models import SessionMetadata

louca = [
    "🤪Su Nivel De Locura es de : 100%", "🤪Su Nivel De Locura es de : 99%",
    "🤪Su Nivel De Locura es de : 50%", "🤪Su nivel De Locura es de : 0%",
    "🤪Su Nivel De Locura es de : 1%", "🤪Su Nivel De Locura es de : 2%",
    "🤪Su Nivel De Locura es de : 64%", "🤪Su Nivel De Locura es de : 22%",
    "🤪Su Nivel De Locura es de : 19%", "🤪Su Nivel De Locura es de : 88%",
    "🤪Su Nivel De Locura es de : 39%", "🤪Su Nivel De Locura es de : 40%",
    "🤪Su Nivel De Locura es de : 92%", "🤪Su Nivel De Locura es de : 74%",
    "🤪Su Nivel De Locura es de : 10%", "🤪Su Nivel De Locura es de : 9%",
    "🤪Su Nivel De Locura es de : 77%", "🤪Su Nivel De Locura es de : 82%",
    "🤪Su Nivel De Locura es de : 66%", "🤪Su Nivel De Locura es de : 11%",
    "🤪Su Nivel De Locura  de : 15%"
]

casa = [
    "Me caso contigo 💍", "Claro Que si 💍❤️", "No quiero 💍💔", "Claro Que No 💍💔",
    "Eu Te Amo, por supuesto quiero casar contigo💍"
]

curativo = [
    "🔴Usaste el vendaje en el que está tu vida: 100%🔴",
    "🔴Usaste el vendaje en el que está tu vida: 50%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 60%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 75%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 85%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 80%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 90%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 95%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 99%🔴",
    "🔴Usaste el vendaje en el que se encuentra tu vida: 91%🔴"
]

bomba = [
    "💣🧟‍♂️ Lanzaste una bomba sobre 1 jefe zombi 🧟‍♀️💣",
    "💣🧟 Lanzaste una bomba a 3x Boss Zombie 🧟💣",
    "💣🧟‍♂️ Lanzaste una bomba sobre 2x Boss Zombie 💣🧟‍♀️",
    "💣🧟‍♂️ Lanzaste una bomba sobre 7x Boss Zombie 💣🧟‍♂️",
    "💣🧟 Lanzaste una bomba a 4x Boss Zombie 🧟💣"
]

facada = [
    "🧟🔪 Apuñalaste a 1 zombi 🔪🧟", "🧟🔪 Apuñalaste a 6 zombis 🔪🧟",
    "🧟🔪 Apuñalaste a siete zombis 🔪🧟", "🧟‍♂️🔪🧟‍♂️ Apuñalaste a 8 zombis 🔪🧟‍♂️",
    "🧟🔪 Apuñalaste a 10 zombis 🔪🧟", "🧟🔪 Apuñalaste a 9 zombis 🔪🧟",
    "🧟‍♀️🔪🧟‍♂️ Apuñalaste a 3 zombis 🧟‍♂️🔪🧟‍♀️"
]

tirar = [
    "🧟Disparaste a 5 zombis🧟", "🧟Disparaste a 1 zombi🧟",
    "🧟Disparaste a 8 zombis🧟", "🧟Disparaste a 3 zombis🧟",
    "🧟‍♂️Disparaste a 5 zombis🧟‍♂️", "🧟‍♀️Disparaste a 10 zombis🧟‍♀️",
    "🧟🧟‍♀️Disparaste 9x zombis🧟🧟‍♀️"
]

play = [
    "🔴Tu vida está al 50% de uso: /curativo",
    "🔴Tu vida es 20% de uso: /curativo",
    "🔴Tu vida está al 40% de uso: /curativo",
    "🧟Vienen los zombis. Utilice: /puñalar o /disparar",
    "🧟🧟‍♂️ Hay muchos zombis 🧟‍♀️🧟 🛡 Usa: /escudo 🛡",
    "🧟Viene el jefe zombi. Usa: /bomb",
    "🧟Vienen los zombis. Utilice: /puñalar o /disparar",
    "🧟🧟‍♂️ Hay muchos zombis 🧟‍♀️🧟 🛡 Usa: /escudo 🛡",
    "🔴Tu Vida Está al 60% de uso : /curativo",
    "🔴Tu vida es 10% de uso: /curativo",
    "🧟Vienen los zombis. Utilice: /puñalar o /disparar",
    "🧟Vienen los zombis. Utilice: /puñalar o /disparar",
    "🧟Vienen los zombis. Utilice: /puñalar o /disparar",
    "🧟Vienen los zombis. Utilice: /puñalar o /disparar",
    "🧟Vienen los zombis. Utilice: /puñalar o /disparar",
    "🧟Vienen los zombis. Usa: /puñalar o /disparar"
]

pescar = [
    "🥈GANASTE LA MEDALLA: PESCADOR DE PLATA🥈",
    "🥉GANASTE LA MEDALLA: PESCADOR DE BRONCE🥉",
    "🥉GANASTE LA MEDALLA: PESCADOR DE BRONCE🥉",
    "🥉GANASTE LA MEDALLA: PESCADOR DE BRONCE🥉",
    "🥉GANASTE LA MEDALLA: PESCADOR DE BRONCE🥉", "  Evento: /carpa   ",
    "⚫️Has pescado 3x Night Moon⚫️(+150 PUNTOS)",
    "⚫️Pescaste 2x Night Moon⚫️(+100 PUNTOS)",
    "⚫️Pescaste 1x Luna Nocturna⚫️(+50 PUNTOS)",
    "   Captaste 1 camarón dorado    (MÚLTIPLES PUNTOS)",
    "   Pescaste 1 platija dorada   (MÚLTIPLES PUNTOS)",
    "  🌈Atrapaste 1 pulpo arcoíris  🌈 (PUNTOS EXTRA)",
    "🐢Atrapaste 3x Tortuga 🐢 (PÉRDIDA DE PUNTOS)",
    "🦑 Captaste 1 calamar gigante 🦑 (LEGENDARIO)",
    "🦀Atrapaste 6x cangrejos 🦀 (COMÚN)", "🦀Atrapaste 2x cangrejos 🦀 (COMÚN)",
    "🦀Atrapaste 8x cangrejos 🦀 (COMÚN)",
    "   Pescaste 1 pulpo de mar   (EPICO)", "🦈 Pescaste 2 tiburones🦈 (EPICO)",
    "🦈 Pescaste 5 tiburones🦈 (EPICO)", "🦈 Pescaste 8 tiburones🦈 (EPICO)",
    "🦈Atrapaste 1 tiburón🦈 (ÉPICO)",
    "🐠 Pescaste 1x atún del mar🐠 (LEGENDARIO)",
    "🐠Atrapaste 3 peces payaso🐠 (LEGENDARIO)",
    "🐠 Pescaste 3x atún del mar🐠 (LEGENDARIO)",
    "🐠Atrapaste 1 pez payaso🐠 (LEGENDARIO)",
    "🐠Atrapaste 8 peces payaso🐠 (LEGENDARIO)",
    "🐠Atrapaste 10 peces payaso🐠 (LEGENDARIO)", "🐟Pescaste 1x salmón🐟 (RARO)",
    "🧜🏼‍♀️Pescaste 5x sirena🧜🏼‍♀️(ÉPICO)",
    "🧜🏼‍♀️Atrapaste 2x sirena🧜🏼‍♀️(EPIC)",
    "🧜🏼‍♀️Atrapaste 1x sirena🧜🏼‍♀️(EPIC)", "🐟Atrapaste 3x salmón🐟 (RARO)",
    "   Pescaste 1x tilapia dorada   (MÚLTIPLES PUNTOS)",
    "☠️🐋Atrapaste 3 ballenas muertas☠️🐋 (PÉRDIDA DE PUNTOS)",
    "🐋Capturaste 11 ballenas del mar🐋(COMÚN)",
    "🐋🌈Atrapaste 1 ballena arcoíris🌈🐋 (PUNTOS EXTRA)",
    "🥈GANASTE LA MEDALLA: PESCADOR DE PLATA🥈",
    "🥇GANASTE LA MEDALLA: PESCADOR DE ORO🥇",
    "🏅GANASTE LA MEDALLA: ESTRELLA DEL PESCADOR🏅", "💎Evento: /camarones💎"
]

cantada = [
    "¿Puedo tomar una foto de usted? Es para mostrarle a Santa lo que quiero como regalo.",
    "Si el negro fuera pasión y el blanco cariño, lo que siento por ti sería cuadros.",
    "¿Cuál es el número de la policía? Desafortunadamente, tendré que denunciarte por robarme el corazón.",
    "Mis amigos me apostaron a que no podría iniciar una conversación con la persona más bonita de aquí. ¿Cómo deberíamos gastar su dinero?",
    "Encantado de conocerte, soy un ladrón. Estoy aquí para robarte el corazón.",
    "Las investigaciones muestran que las personas juntas son un error gramatical, pero las personas separadas son errores del destino.",
    "Si nada dura para siempre ¿quieres ser mi nada?",
    "¿Tu nombre es Wi-Fi? Porque siento una conexión aquí.",
    "¿Ves esa estrella de allí? Lo hice colgar para ti.",
    "Entonces, además de dejarme sin aliento, ¿qué más haces?",
    "¡Vaya, tengo dolor en el pecho! Espero que sea amor, porque si es un infarto, ¡nunca te volveré a ver!",
    "Las rosas son rojas, las violetas son azules, no sé rimar, pero ¿puedo salir contigo?",
    "¿Estabas hecho con velas, miel, lazos rojos y rosas? Porque te encontré lindo."
]

chiste = [
    "¿Cuál es el plato favorito de Thor? Thorresmo",
    "¿Qué hizo el caballo en la cabina telefónica? Ir al trote",
    "¿Cuál es el río más ácido del mundo? El río Solimões",
    "¿Cuál es el mejor lugar de Brasil? El interior del país.",
    "¿Qué vino no tiene alcohol? Vino de codorniz",
    "Habia una ves unperrito q se llamaba pegamneto, se cayo y se pego""
]

hate = [
    "La gente te odia 0%", "La gente te odia 20%", "La gente te odia al 100%",
    "La gente te odia al 50%", "La gente te odia el 45%",
    "La gente te odia el 99%", "La gente te odia el 95%",
    "La gente te odia el 34%", "La gente te odia 77%", "La gente te odia 80%",
    "La gente te odia 66%", "La gente te odia 39%", "La gente te odia un 20%",
    "La gente te odia un 22%", "La gente te odia 49%"
]

amor = [
    "La gente te ama 0%❤️", "La gente te ama 20%❤️",
    "La gente te quiere al 100%❤️", "La gente te quiere al 50%❤️",
    "La gente te ama 45%❤️", "La gente te ama 99%❤️", "La gente te ama 95%❤️",
    "La gente te ama 34%❤️", "La gente te quiere 77%❤️",
    "La gente te quiere 80%❤️", "La gente te ama 66%❤️",
    "La gente te ama 39%❤️", "La gente te ama un 20%❤️",
    "La gente te ama un 22%❤️", "La gente te ama 49%❤️"
]


class Bot(BaseBot):

  async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("en funcionamiento")
    await self.highrise.walk_to(Position(14.5, 0.25, 10.5, "FrontLeft"))

  async def on_user_join(self, user: User,
                         position: Position | AnchorPosition) -> None:
    print(f"{user.username} ha entrado a la sala")
    await self.highrise.send_whisper(user.id,
                                     f"Bienvenido a un lugar tranquilo {user.username}!")
    await self.highrise.send_whisper(
        user.id, f"No olvides portarte bien {user.username}!")

    await self.highrise.send_emote("dance-tiktok11")

    await self.highrise.send_emote("dance-tiktok11", user.id)

  async def on_chat(self, user: User, message: str) -> None:
    print(f"{user.username}: {message}")

    if message.startswith("/pescar"):
      await self.highrise.send_whisper(user.id, "Estás pescando 🎣...")

    if message.lower() == "/pescar":
      frase = random.choice(pescar)
      await self.highrise.send_whisper(user.id, frase)

    if message.lower() == "/bomba":
      frase = random.choice(bomba)
      await self.highrise.send_whisper(user.id, frase)
    if message.lower() == "/facada":
      frase = random.choice(facada)
      await self.highrise.send_whisper(user.id, frase)
    if message.lower() == "/curativo":
      frase = random.choice(curativo)
      await self.highrise.send_whisper(user.id, frase)
    if message.lower() == "/play":
      frase = random.choice(play)
      await self.highrise.send_whisper(user.id, frase)
    if message.lower() == "/tirar":
      frase = random.choice(atirar)
      await self.highrise.send_whisper(user.id, frase)

    if message.lower() == "/mi nivel de locura":
      frase = random.choice(louca)
      await self.highrise.send_whisper(user.id, frase)

    if message.lower() == "/casa?":
      frase = random.choice(casa)
      await self.highrise.chat(frase)

    if message.startswith("/pescar"):
      await self.highrise.react("clap", user.id)

    if message.startswith("/carpa"):
      await self.highrise.react("clap", user.id)
      await self.highrise.send_whisper(
          user.id,
          "  🤑Atrapaste 1x Carpa Dorada   GANASTE LA MEDALLA: (MEGA PESCADOR)🤑"
      )

    if message.startswith("camaron"):
      await self.highrise.react("clap", user.id)
      await self.highrise.send_whisper(
          user.id,
          "💎Atrapaste 1x camarón diamante💎GANASTE LA MEDALLA: (MAESTRO PESCADOR DIAMANTE)"
      )
    if message.startswith("/curativo"):
      await self.highrise.react("heart", user.id)

    if message.startswith("/escudo"):
      await self.highrise.react("heart", user.id)
      await self.highrise.send_whisper(
          user.id, f"@{user.username} 🛡 Usaste el escudo🛡")

    if message.lower() == "/cuantas personas me aman":
      frase = random.choice(amor)
      await self.highrise.send_whisper(user.id, frase)

    if message.lower() == "/cuanta gente me odia":
      frase = random.choice(hate)
      await self.highrise.send_whisper(user.id, frase)

    if message.lower() == "/chiste":
      frase = random.choice(chiste)
      await self.highrise.chat(frase)

    if message.lower() == "/cantada":
      frase = random.choice(cantada)
      await self.highrise.chat(frase)

    if message.startswith("/tele") or message.startswith(
        "/tp") or message.startswith("/fly") or message.startswith(
            "!tele") or message.startswith("!tp") or message.startswith("!fly"):
      if user.username == "aex_savage_":
        await self.teleporter(message)

    if message.startswith("/") or message.startswith(
        "-") or message.startswith(".") or message.startswith("!"):
      await self.command_handler(user, message)

    if message.startswith("!emoteall"):
      await self.highrise.send_whisper(
          user.id,
          "Fashion All , Wrong All , Cutey All , Superpose All , Punk All , Tiktok2 All, Tiktok8 All , Tiktok9 All , Tiktok10 All , Gagging All , Blackpink All , Creepy All , Revelation All , Bashful All , Arabesque All , Party All"
      )

    if message.startswith("!emoteall"):
      await self.highrise.send_whisper(
          user.id,
          "Pose3 All , Pose7 All , Pose5 All , Pose1 All , Enthused All , Pose8 All , Sing All , Teleport All , Telekinesis All , Casual All , Icecream All , Watch All"
      )

    if message.startswith("!emoteall"):
      await self.highrise.send_whisper(
          user.id,
          "Zombie All , Celebrate All , Kiss All , Bow All , Snowangel All , Confused All , Charging All , Wei All , Cursing All , Greedy All , Russian All , Shop All , Model All , Ren All , Tiktok4 All , Snake All , Uwu All"
      )

    if message.startswith("!emoteall"):
      await self.highrise.send_whisper(
          user.id,
          "Skating All , Time All , Gottago All  , Scritchy All , Bitnervous All , Jingle All , Curtsy All , Hot All , Hyped All ,Sleigh All , Surprise All, Repose All , Kawaii All , Touch All , Gift All , Pushit All , Tiktok All , Smooch All , Launch All"
      )

    if message.startswith("/emote-id"):
      await self.highrise.send_whisper(
          user.id,
          "emote-gravity , idle-uwu , idle-enthusiastic , emote-kiss , emote-float , idle_singing , emote-cute , emote-pose7 , emote-pose8 , emote-fashionista , emote-creepycute , emote-headblowup , emote-shy2 , emote-celebrate , idle-nervous , idle-wild"
      )

    if message.startswith("/emote-id"):
      await self.highrise.send_whisper(
          user.id,
          "emote-gift , dance-touch , dance-employee , dance-tiktok11 , emote-salute"
      )

    if message.startswith("!lista") or message.startswith("!list"):
      await self.highrise.send_whisper(
          user.id,
          "!angry ,!thumbsup , !cursing , !flex , !gagging , !celebrate , !blackpink , !tiktok2 , !tiktok9 , !pennywise , !russian , !shop , !enthused , !singing ,!wrong , !guitar , !pinguin , !astronaut , !saunter , !flirt , !creepy , !watch , !revelation"
      )

    if message.startswith("!lista") or message.startswith("!list"):
      await self.highrise.send_whisper(
          user.id,
          "!tiktok10 ,!tiktok8 , !cutey , !pose3 , !pose5 , !pose1 , !pose8 , !pose7  !pose9 , !cute , !superpose , !frog , !snake , !energyball , !maniac , !teleport , !float , !telekinesi , !fight , !wei , !fashion , !boxer , !bashful , !arabesque , !party"
      )

    if message.startswith("!lista") or message.startswith("!list"):
      await self.highrise.send_whisper(
          user.id,
          "!confused , !charging , !snowangel , !hot , !snowball , !curtsy , !bow ,!model , !greedy , !tired , !shy , !wave , !hello , !lau ,!yes , !sad , !no , !kiss , !casual , !ren , !sit , !punk , !zombie , !gravity , !icecream ,!uwu , !sayso , !star"
      )

    if message.startswith("!lista") or message.startswith("!list"):
      await self.highrise.send_whisper(
          user.id,
          "!skating , !bitnervous , !scritchy , !timejump , !gottago , !jingle , !hyped , !sleigh , !surprise , !repose , !kawaii , !touch , !gift , !pushit , !tiktok , !salute , !attention , !smooch , !launch"
      )

    if message.startswith("/lista") or message.startswith("/list"):
      await self.highrise.send_whisper(
          user.id,
          "/angry ,/thumbsup , /cursing , /flex , /gagging , /celebrate , /blackpink , /tiktok2 , /tiktok9 , /pennywise , /russian , /shop , /enthused , /singing , /wrong , /guitar , /pinguin , /astronaut , /saunter , /flirt , /creepy , /watch , /revelation"
      )

    if message.startswith("/lista") or message.startswith("/list"):
      await self.highrise.send_whisper(
          user.id,
          "/tiktok10 , /tiktok8 , /cutey , /pose3 , /pose5 , /pose1 , /pose8 , /pose7  /pose9 , /cute , /superpose , /frog , /snake , /energyball , /maniac , /teleport , /float , /telekinesi , /fight , /wei , /fashion , /boxer , /bashful , /arabesque , /party"
      )

    if message.startswith("/lista") or message.startswith("/list"):
      await self.highrise.send_whisper(
          user.id,
          "/confused , /charging , /snowangel , /hot , /snowball , /curtsy , /bow ,/model , /greedy , /lust , /tired , /shy , /wave , /hello , /lau , /yes , /sad , /no , /kiss , /casual , /ren ,   /sit , /punk , /zombie , /gravity , /icecream ,/uwu , /sayso , /star"
      )

    if message.startswith("/lista") or message.startswith("/list"):
      await self.highrise.send_whisper(
          user.id,
          "/skating , /bitnervous , /scritchy , /timejump , /gottago , /jingle , /hyped , /sleigh , /surprise , /repose , /kawaii /touch , /pushit , /gift , /tiktok , /salute , /attention , /smooch , /launch"
      )

    if message.startswith("/lista") or message.startswith(
        "!emoteall") or message.startswith("!lista"):
      await self.highrise.send_emote("dance-floss")

    if message.startswith("Feo") or message.startswith(
        "feo") or message.startswith("Pobre") or message.startswith("pobre"):
      await self.highrise.chat(f"RESPETE!!! {user.username} 🤬🤬")
      await self.highrise.send_emote("emote-swordfight")

    if message.startswith("estupido") or message.startswith(
        "subnormal") or message.startswith("Vagabundo") or message.startswith("comepinga") or message.startswith(
            "vagabundo"):
      await self.highrise.chat(f"TU MADRE!!! {user.username} 🤬🤬")
      await self.highrise.send_emote("emote-swordfight")

    if message.startswith("personas") or message.startswith("!personas"):
      room_users = (await self.highrise.get_room_users()).content
      await self.highrise.chat(f"Hay  {len(room_users)} personas en la sala ")
      await self.highrise.send_emote("dance-floss")

    if message.startswith("caliente") or message.startswith(
        "Gostoso") or message.startswith("GOSTOSO"):
      await self.highrise.send_emote("idle-uwu")
      await self.highrise.send_emote("idle-uwu", user.id)
      await self.highrise.chat(f"tu tambien estas caliente {user.username} 😳👉👈"
                               )

    if message.startswith("emotes") or message.startswith("/emotes"):
      await self.highrise.send_emote("emote-robot")
      await self.highrise.send_whisper(
          user.id, f"gestos disponibles del número 1 al 95")

    if message.startswith("Help") or message.startswith(
        "/help") or message.startswith("!help") or message.startswith("help"):
      await self.highrise.chat(
          f"/lista , !lista , personas,  emotes, user-info  , /emote-id , !emoteaall"
      )
      await self.highrise.chat(
          f"{user.username} 🥰 Grasias por hacer de esta su casa")
      await self.highrise.send_emote("dance-floss")

    if message.startswith("Lindo") or message.startswith(
        "LINDO") or message.startswith("lindo"):
      await self.highrise.react(
          "heart",
          user.id,
      )
      await self.highrise.chat(
          f"tú también eres muy lind(a) {user.username} 🥰🥰")
      await self.highrise.send_emote("emote-shy")

    if message.startswith("palma"):
      await self.highrise.react("clap", user.id)

    if message.startswith("Buen dia") or message.startswith(
        "Buenos Dias") or message.startswith("buen dia") or message.startswith(
            "buenos dias"):
      await self.highrise.send_emote("emote-tapdance")
      await self.highrise.send_whisper(user.id, f"Buen Dia {user.username} 😊🌅")

    if message.startswith("Buenas noches") or message.startswith(
        "buenas noches") or message.startswith(
            "Linda noche") or message.startswith("linda noche"):
      await self.highrise.send_emote("dance-singleladies")
      await self.highrise.send_whisper(user.id,
                                       f"Buenas noches {user.username} 😊🌃🌉")

    if message.startswith("Buenas tardes") or message.startswith(
        "buenas tardes") or message.startswith(
            "Boa Tarde") or message.startswith("BUENAS TARDES"):
      await self.highrise.send_emote("emote-monster_fail")
      await self.highrise.send_whisper(user.id,
                                       f"Buenas Tardes {user.username} ☀️")

    if message.startswith("😡") or message.startswith(
        "🤬") or message.startswith("😤") or message.startswith(
            "🤨") or message.startswith("😒") or message.startswith("🙄"):
      await self.highrise.send_emote("emote-boxer", user.id)

    if message.startswith("🤔") or message.startswith(
        "🧐") or message.startswith("🥸") or message.startswith(
            "🫤") or message.startswith("😕"):
      await self.highrise.send_emote("emote-confused", user.id)

    if message.startswith("🤣") or message.startswith(
        "😂") or message.startswith("😁") or message.startswith("😀"):
      await self.highrise.send_emote("emote-laughing", user.id)

    if message.startswith("😗") or message.startswith(
        "😘") or message.startswith("😙") or message.startswith(
            "💋") or message.startswith("😚"):
      await self.highrise.send_emote("emote-kiss", user.id)

    if message.startswith("😊") or message.startswith(
        "🥰") or message.startswith("😳") or message.startswith("🤗"):
      await self.highrise.send_emote("idle-uwu", user.id)

    if message.startswith("🤢") or message.startswith(
        "🤮") or message.startswith("🤧") or message.startswith(
            "😵‍💫") or message.startswith("🤒"):
      await self.highrise.send_emote("emoji-gagging", user.id)

    if message.startswith("😱") or message.startswith(
        "😬") or message.startswith("😰") or message.startswith(
            "😫") or message.startswith("😨"):
      await self.highrise.send_emote("idle-nervous", user.id)

    if message.startswith("🤯"):
      await self.highrise.send_emote("emote-headblowup", user.id)

    if message.startswith("☺️") or message.startswith(
        "🫣") or message.startswith("😍") or message.startswith(
            "🥺") or message.startswith("🥹"):
      await self.highrise.send_emote("emote-shy2", user.id)

    if message.startswith("😏") or message.startswith("😈"):
      await self.highrise.send_emote("emote-lust", user.id)

    if message.startswith("🥵") or message.startswith("🫠"):
      await self.highrise.send_emote("emote-hot", user.id)

    if message.startswith("/thumbs") or message.startswith(
        "👍") or message.startswith("!thumbs") or message.startswith(
            "Thumbs") or message.startswith("Like"):
      await self.highrise.chat(f"👍 para {user.username}")
      await self.highrise.react("thumbs", user.id)
    if message.startswith("/clap") or message.startswith(
        "!clap") or message.startswith("Clap") or message.startswith(
            "👏") or message.startswith("Palma"):
      await self.highrise.react("clap", user.id)
      await self.highrise.chat(f"👏 para {user.username}")

    if message.startswith("Saluda") or message.startswith(
        "!wave") or message.startswith("👋") or message.startswith(
            "wave") or message.startswith("Saludo"):
      await self.highrise.react("wave", user.id)
      await self.highrise.chat(f"👋 para {user.username}")

    if message.startswith("heart") or message.startswith(
        "!heart") or message.startswith("Heart") or message.startswith(
            "❤️") or message.startswith("Amor"):
      await self.highrise.react("heart", user.id)
      await self.highrise.chat(f"❤️ para {user.username}")

    if message.startswith("guiñar") or message.startswith(
        "😉") or message.startswith("wink") or message.startswith(
            "😉") or message.startswith("Piscar"):
      await self.highrise.react("wink", user.id)
      await self.highrise.chat(f"😉 para {user.username}")

    if message.startswith("!wrong") or message.startswith(
        "/wrong") or message.startswith("Wrong") or message.startswith("1"):
      await self.highrise.send_emote("dance-wrong", user.id)
      await self.highrise.chat(f"Cómo Mola {user.username} Presumid@ wtf 🥵")

    if message.startswith("/fashion") or message.startswith(
        "!fashion") or message.startswith("Fashion") or message.startswith(
            "2"):
      await self.highrise.send_emote("emote-fashionista", user.id)
      await self.highrise.chat(
          f" Ya ya {user.username} deja de hacerte el millonario😨")

    if message.startswith("/gravity") or message.startswith(
        "!gravity") or message.startswith("Gravity") or message.startswith(
            "3"):
      await self.highrise.send_emote("emote-gravity", user.id)
      await self.highrise.chat(
          f" Oye tu {user.username} Para de hacer el gili pobre☺️")

    if message.startswith("/icecream") or message.startswith(
        "!icecream") or message.startswith("Icecream") or message.startswith(
            "4"):
      await self.highrise.send_emote("dance-icecream", user.id)
      await self.highrise.chat(
          f" Osea mira {user.username} jajaja que pena contigo por dios😂")

    if message.startswith("/casual") or message.startswith(
        "!casual") or message.startswith("Casual") or message.startswith("5"):
      await self.highrise.send_emote("idle-dance-casual", user.id)
      await self.highrise.chat(
          f" Pfff vaya hambriento de {user.username} jajaja asco totat💰")

    if message.startswith("/kiss") or message.startswith(
        "!kiss") or message.startswith("Kiss") or message.startswith("6"):
      await self.highrise.send_emote("emote-kiss", user.id)
      await self.highrise.chat(f" Oye Marica {user.username} Deja eso mamón🥺")

    if message.startswith("/no") or message.startswith(
        "!no") or message.startswith("No") or message.startswith("7"):
      await self.highrise.send_emote("emote-no", user.id)
      await self.highrise.chat(f" Que miel {user.username} joder para para 😜")

    if message.startswith("/sad") or message.startswith(
        "!sad") or message.startswith("Sad") or message.startswith("8"):
      await self.highrise.send_emote("emote-sad", user.id)
      await self.highrise.chat(
          f" Mirad al {user.username} Más pobre que mi prima jajaja👑")

    if message.startswith("/si") or message.startswith(
        "!yes") or message.startswith("Si") or message.startswith("9"):
      await self.highrise.send_emote("emote-yes", user.id)
      await self.highrise.chat(
          f" Dios mio {user.username} que calvo tu estas pff🙂")

    if message.startswith("/lau") or message.startswith(
        "!lau") or message.startswith("Lau") or message.startswith("10"):
      await self.highrise.send_emote("emote-laughing", user.id)
      await self.highrise.chat(
          f" La madre que te cogio {user.username} miel joe😗")

    if message.startswith("/hola") or message.startswith(
        "!hello") or message.startswith("Hola") or message.startswith("11"):
      await self.highrise.send_emote("emote-hello", user.id)
      await self.highrise.chat(
          f" Oye Mamacoñi tu {user.username} deja eso Pobretón😁")

    if message.startswith("/wave") or message.startswith(
        "!wave") or message.startswith("Wave") or message.startswith("12"):
      await self.highrise.send_emote("emote-wave", user.id)
      await self.highrise.chat(
          f" No puedes conmigo {user.username} lastima jajaja😆")

    if message.startswith("/shy") or message.startswith(
        "!shy") or message.startswith("Shy") or message.startswith("13"):
      await self.highrise.send_emote("emote-shy", user.id)
      await self.highrise.chat(
          f" Jajaja perdedor de {user.username} no lo vas a lograr🤪")

    if message.startswith("/Tired") or message.startswith(
        "!Tired") or message.startswith("Tired") or message.startswith("14"):
      await self.highrise.send_emote("emote-tired", user.id)
      await self.highrise.chat(f" Oye Basura {user.username} Tranqui Ptm coñ🫠")

    if message.startswith("/flirt") or message.startswith(
        "!flirt") or message.startswith("Flirt") or message.startswith(
            "/Flirty") or message.startswith("!Flirty") or message.startswith(
                "Flirty") or message.startswith(
                    "!flirtywave") or message.startswith(
                        "/flirtywave") or message.startswith(
                            "Flirtywave") or message.startswith("15"):
      await self.highrise.send_emote("emote-lust", user.id)
      await self.highrise.chat(
          f" Tu pt ma' {user.username} no ves lo que haces gay")

    if message.startswith("/greedy") or message.startswith(
        "!greedy") or message.startswith("Greedy") or message.startswith("16"):
      await self.highrise.send_emote("emote-greedy", user.id)
      await self.highrise.chat(f" Oye {user.username} mereces el infierno hdp😡"
                               )

    if message.startswith("/model") or message.startswith(
        "!model") or message.startswith("Model") or message.startswith("17"):
      await self.highrise.send_emote("emote-model", user.id)
      await self.highrise.chat(
          f" Que verga {user.username} mamaguevo digo glugluglu🤗")

    if message.startswith("/bow") or message.startswith(
        "!bow") or message.startswith("Bow") or message.startswith("18"):
      await self.highrise.send_emote("emote-bow", user.id)
      await self.highrise.chat(
          f" Nmms la chingada de tu hija {user.username} diablo loco🤬")

    if message.startswith("/curtsy") or message.startswith(
        "!curtsy") or message.startswith("Curtsy") or message.startswith("19"):
      await self.highrise.send_emote("emote-curtsy", user.id)
      await self.highrise.chat(
          f" Seria tu fan {user.username} pero hueles como el culaso🤡")

    if message.startswith("/snowball") or message.startswith(
        "!snowball") or message.startswith("Snowball") or message.startswith(
            "20"):
      await self.highrise.send_emote("emote-snowball", user.id)
      await self.highrise.chat(
          f" Eeeeeh tuuuu {user.username} te picaron las moscas o que para joe la pt😳"
      )

    if message.startswith("/hot") or message.startswith(
        "!hot") or message.startswith("Hot") or message.startswith("21"):
      await self.highrise.send_emote("emote-hot", user.id)
      await self.highrise.chat(
          f" Tu eh eh {user.username} tomese un refresco para enfriar cbrn😵")

    if message.startswith("/snowangel") or message.startswith(
        "!snowangel") or message.startswith("Snowangel") or message.startswith(
            "22"):
      await self.highrise.send_emote("emote-snowangel", user.id)
      await self.highrise.chat(
          f" Que pasa {user.username} Problems o que basurero🥶")

    if message.startswith("/charging") or message.startswith(
        "!charging") or message.startswith("Charging") or message.startswith(
            "23"):
      await self.highrise.send_emote("emote-charging", user.id)
      await self.highrise.chat(
          f" Cuidado no lo hagas encima {user.username} cabeza de vaca🤢")

    if message.startswith("/confused") or message.startswith(
        "!confused") or message.startswith("Confused") or message.startswith(
            "24"):
      await self.highrise.send_emote("emote-confused", user.id)
      await self.highrise.chat(
          f" Chacho cñ {user.username} Te la estan cogiendo o que, lavate jode🤕"
      )

    if message.startswith("/telekinesis") or message.startswith(
        "!telekinesis") or message.startswith(
            "Telekinesis") or message.startswith("25"):
      await self.highrise.send_emote("emote-telekinesis", user.id)
      await self.highrise.chat(
          f" Tranqui sin miedo {user.username} no muerdo cabra👺")

    if message.startswith("/float") or message.startswith(
        "!float") or message.startswith("Float") or message.startswith("26"):
      await self.highrise.send_emote("emote-float", user.id)
      await self.highrise.chat(
          f" Ven aca {user.username} que es lo que tu te piensas🎃")

    if message.startswith("/teleport") or message.startswith(
        "!teleport") or message.startswith("Teleport") or message.startswith(
            "27"):
      await self.highrise.send_emote("emote-teleporting", user.id)
      await self.highrise.chat(
          f" Que haces tú  {user.username} deja de mirar el pack de otros gay🙉"
      )

    if message.startswith("/maniac") or message.startswith(
        "!maniac") or message.startswith("Maniac") or message.startswith("28"):
      await self.highrise.send_emote("emote-maniac", user.id)
      await self.highrise.chat(
          f" Lo viste? {user.username} quiere decir qe estas afónico 💩")

    if message.startswith("/energyball") or message.startswith(
        "!energyball") or message.startswith(
            "Energyball") or message.startswith("29"):
      await self.highrise.send_emote("emote-energyball", user.id)
      await self.highrise.chat(f" Que pdo {user.username} estate quieto ya🤖")

    if message.startswith("/snake") or message.startswith(
        "!snake") or message.startswith("Snake") or message.startswith("30"):
      await self.highrise.send_emote("emote-snake", user.id)
      await self.highrise.chat(
          f" Que asco muchacho {user.username} te crees mucho siendo bot xd🌜")

    if message.startswith("/frog") or message.startswith(
        "!frog") or message.startswith("Frog") or message.startswith("31"):
      await self.highrise.send_emote("emote-frog", user.id)
      await self.highrise.chat(
          f" Como te gusta eh {user.username} 💦")

    if message.startswith("/superpose") or message.startswith(
        "!superpose") or message.startswith("Superpose") or message.startswith(
            "32"):
      await self.highrise.send_emote("emote-superpose", user.id)
      await self.highrise.chat(f" Ptm la k te cogio ayer {user.username} 🥵")

    if message.startswith("/cute") or message.startswith(
        "!cute") or message.startswith("Cute") or message.startswith("33"):
      await self.highrise.send_emote("emote-cute", user.id)
      await self.highrise.chat(
          f" Con esa cara {user.username} tu que vas a saber💨")

    if message.startswith("/pose7") or message.startswith(
        "!pose7") or message.startswith("Pose7") or message.startswith("34"):
      await self.highrise.send_emote("emote-pose7", user.id)
      await self.highrise.chat(
          f" Sal de aquí cñ ya {user.username} fuera ya pero ya💥")

    if message.startswith("/pose8") or message.startswith(
        "!pose8") or message.startswith("Pose8") or message.startswith("35"):
      await self.highrise.send_emote("emote-pose8", user.id)
      await self.highrise.chat(
          f" Que te pasa {user.username} no te lo habran colgado no? jaja💝")

    if message.startswith("/pose1") or message.startswith(
        "!pose1") or message.startswith("Pose1") or message.startswith("36"):
      await self.highrise.send_emote("emote-pose1", user.id)
      await self.highrise.chat(
          f" Te dio un calambre? {user.username} Madre mia, mañana mas x gay🔥")

    if message.startswith("/pose5") or message.startswith(
        "!pose5") or message.startswith("Pose5") or message.startswith("37"):
      await self.highrise.send_emote("emote-pose5", user.id)
      await self.highrise.chat(
          f" Asere, q hay {user.username} te gusto lo riko q esta o q?🎉")

    if message.startswith("/pose3") or message.startswith(
        "!pose3") or message.startswith("Pose3") or message.startswith("38"):
      await self.highrise.send_emote("emote-pose3", user.id)
      await self.highrise.chat(
          f" La concha de su hija {user.username} que hijo de fruta🎉")

    if message.startswith("/cutey") or message.startswith(
        "!cutey") or message.startswith("Cutey") or message.startswith("39"):
      await self.highrise.send_emote("emote-cutey", user.id)
      await self.highrise.chat(
          f" Oye hijito {user.username} no te inflen por dios, carajo👄")

    if message.startswith("/tik10") or message.startswith(
        "!tik10") or message.startswith("Tik10") or message.startswith("40"):
      await self.highrise.send_emote("dance-tiktok10", user.id)
      await self.highrise.chat(
          f" Santo cielo de mi vida {user.username} k sucio buaj🗣️")

    if message.startswith("/sing") or message.startswith(
        "!sing") or message.startswith("Sing") or message.startswith(
            "Singing") or message.startswith("/singing") or message.startswith(
                "!singing") or message.startswith("41"):
      await self.highrise.send_emote("idle_singing", user.id)
      await self.highrise.chat(
          f" Te meten un pepino {user.username} es como estar en su cama ofreciendo jajaj👀"
      )

    if message.startswith("/enthused") or message.startswith(
        "!enthused") or message.startswith("Enthused") or message.startswith(
            "42"):
      await self.highrise.send_emote("idle-enthusiastic", user.id)
      await self.highrise.chat(
          f" El diablo {user.username} estas bie? te veo sudando 😂")

    if message.startswith("/shop") or message.startswith(
        "!shop") or message.startswith("Shop") or message.startswith("43"):
      await self.highrise.send_emote("dance-shoppingcart", user.id)
      await self.highrise.chat(
          f" Ay k riko {user.username} me gusto, quiero mas porfa🦴")

    if message.startswith("/russian") or message.startswith(
        "!russian") or message.startswith("Russian") or message.startswith(
            "44"):
      await self.highrise.send_emote("dance-russian", user.id)
      await self.highrise.chat(
          f" Camarada {user.username} У тебя вообще есть эта эмоция?💅🏼")

    if message.startswith("/pennywise") or message.startswith(
        "!pennywise") or message.startswith("Pennywise") or message.startswith(
            "45"):
      await self.highrise.send_emote("dance-pennywise", user.id)
      await self.highrise.chat(f" Besense señor Juan y {user.username} 🥵👀")

    if message.startswith("/tik2") or message.startswith(
        "!tik2") or message.startswith("Tik2") or message.startswith("46"):
      await self.highrise.send_emote("dance-tiktok2", user.id)
      await self.highrise.chat(
          f" Te la ganaste {user.username} chankletazo k te llevas🫵🏼")

    if message.startswith("/blackpink") or message.startswith(
        "!blackpink") or message.startswith("Blackpink") or message.startswith(
            "47"):
      await self.highrise.send_emote("dance-blackpink", user.id)
      await self.highrise.chat(
          f" Jajaja no te creo ni yo {user.username} mentioso de miel🙅🏼")

    if message.startswith("/celebrate") or message.startswith(
        "!celebrate") or message.startswith("Celebrate") or message.startswith(
            "48"):
      await self.highrise.send_emote("emoji-celebrate", user.id)
      await self.highrise.chat(
          f" Ya que estamos {user.username} porque no cogernos 🥺")

    if message.startswith("/gagging") or message.startswith(
        "!gagging") or message.startswith("Gagging") or message.startswith(
            "49"):
      await self.highrise.send_emote("emoji-gagging", user.id)
      await self.highrise.chat(
          f" Vete a tomar x saco {user.username} que te den x alla🧖🏼")

    if message.startswith("/flex") or message.startswith(
        "!flex") or message.startswith("Flex") or message.startswith("50"):
      await self.highrise.send_emote("emoji-flex", user.id)
      await self.highrise.chat(
          f" Deja la pj ya {user.username} ve a trabajar, pinga loco🧘🏼")

    if message.startswith("/cursing") or message.startswith(
        "!cursing") or message.startswith("Cursing") or message.startswith(
            "51"):
      await self.highrise.send_emote("emoji-cursing", user.id)
      await self.highrise.chat(
          f" Oye sobrino {user.username} tráeme agua k me ahogo de tu riqueza corporal🏂🏼"
      )

    if message.startswith("/thumbsup") or message.startswith(
        "!thumbsup") or message.startswith("Thumbsup") or message.startswith(
            "52"):
      await self.highrise.send_emote("emoji-thumbsup", user.id)
      await self.highrise.chat(
          f" No se porque {user.username} pero te veo como mi pollo 😨")

    if message.startswith("/angry") or message.startswith(
        "!angry") or message.startswith("Angry") or message.startswith("53"):
      await self.highrise.send_emote("emoji-angry", user.id)
      await self.highrise.chat(
          f" Mira triste el {user.username} jajaja niñita🧟")

    if message.startswith("/punk") or message.startswith(
        "!punk") or message.startswith("Punk") or message.startswith("54"):
      await self.highrise.send_emote("emote-punkguitar", user.id)
      await self.highrise.chat(
          f" Eh eh macho {user.username} sal de ahi te los coloco🧌")

    if message.startswith("/zombie") or message.startswith(
        "!zombie") or message.startswith("Zombie") or message.startswith("55"):
      await self.highrise.send_emote("emote-zombierun", user.id)
      await self.highrise.chat(
          f" y ese Pack uff {user.username} damelo q me calenté xd🏊🏼")

    if message.startswith("/sit") or message.startswith(
        "!sit") or message.startswith("Sit") or message.startswith("56"):
      await self.highrise.send_emote("idle-loop-sitfloor", user.id)
      await self.highrise.chat(f" Asi te quiero {user.username} 🥵 jajaja riko🤽🏼")

    if message.startswith("/fight") or message.startswith(
        "!fight") or message.startswith("Fight") or message.startswith("57"):
      await self.highrise.send_emote("emote-swordfight", user.id)
      await self.highrise.chat(
          f" Querés pelea o que {user.username} tomala pto👰🏼")

    if message.startswith("/ren") or message.startswith(
        "!ren") or message.startswith("Ren") or message.startswith("58"):
      await self.highrise.send_emote("dance-macarena", user.id)
      await self.highrise.chat(
          f" Te salvaste {user.username} te lo iba a clavar, anda apretado👯")

    if message.startswith("/wei") or message.startswith(
        "!wei") or message.startswith("Wei") or message.startswith("59"):
      await self.highrise.send_emote("dance-weird", user.id)
      await self.highrise.chat(
          f" Que no vuelvas {user.username} te mato con mi cuchillo afilado🧓🏼")

    if message.startswith("/tik8") or message.startswith(
        "!tik8") or message.startswith("Tik8") or message.startswith(
            "/savage") or message.startswith("!savage") or message.startswith(
                "Savage") or message.startswith("60"):
      await self.highrise.send_emote("dance-tiktok8", user.id)
      await self.highrise.chat(
          f" Un placer Sr {user.username} Uy y esa cara de bobo que me llevas jajaj pobre🧑🏼‍🍼"
      )

    if message.startswith("/tik9") or message.startswith(
        "!tik9") or message.startswith("Tik9") or message.startswith(
            "/viral") or message.startswith("!viral") or message.startswith(
                "Viral") or message.startswith("61"):
      await self.highrise.send_emote("dance-tiktok9", user.id)
      await self.highrise.chat(
          f" Vete al moño {user.username} que te lo den alla jaja🏞️")

    if message.startswith("/uwu") or message.startswith(
        "!uwu") or message.startswith("Uwu") or message.startswith("62"):
      await self.highrise.send_emote("idle-uwu", user.id)
      await self.highrise.chat(
          f" No gracias {user.username} Pareces un otaku k pena asco pff🦕")

    if message.startswith("/tik4") or message.startswith(
        "!tik4") or message.startswith("Tik4") or message.startswith(
            "/sayso") or message.startswith("!sayso") or message.startswith(
                "Sayso") or message.startswith("63"):
      await self.highrise.send_emote("idle-dance-tiktok4", user.id)
      await self.highrise.chat(
          f" Uy ese baile riko jaja {user.username} bailame mamii🦓")

    if message.startswith("/star") or message.startswith(
        "!star") or message.startswith("Star") or message.startswith("64"):
      await self.highrise.send_emote("emote-stargazer", user.id)
      await self.highrise.chat(
          f" oleee mira mira  {user.username} ahi esta tu heterosidad jajaja🥰")

    if message.startswith("/pose9") or message.startswith(
        "!pose9") or message.startswith("Pose9") or message.startswith("65"):
      await self.highrise.send_emote("emote-pose9", user.id)
      await self.highrise.chat(
          f" Se congelo jajaja ay {user.username} K te violiii-n jja😍")

    if message.startswith("/box") or message.startswith(
        "!box") or message.startswith("Box") or message.startswith("66"):
      await self.highrise.send_emote("emote-boxer", user.id)
      await self.highrise.chat(
          f" Muchacho ya {user.username} asqueroso vete al vertedero coñ😘")

    if message.startswith("/guitar") or message.startswith(
        "!guitar") or message.startswith("Guitar") or message.startswith("67"):
      await self.highrise.send_emote("idle-guitar", user.id)
      await self.highrise.chat(
          f" Vete mejor por ahi {user.username}, lo gay en otro lado😁")

    if message.startswith("/penguin") or message.startswith(
        "!penguin") or message.startswith("Penguin") or message.startswith(
            "68"):
      await self.highrise.send_emote("dance-pinguin", user.id)
      await self.highrise.chat(
          f" Tu chama es {user.username}? porque me gustas bien rika🥵")

    if message.startswith("/astronaut") or message.startswith(
        "!astronaut") or message.startswith("Astronaut") or message.startswith(
            "69"):
      await self.highrise.send_emote("emote-astronaut", user.id)
      await self.highrise.chat(
          f" Tus Nalgas son ricas  {user.username} pero delgadas🥹")

    if message.startswith("/saunter") or message.startswith(
        "!saunter") or message.startswith("Saunter") or message.startswith(
            "/anime") or message.startswith("!anime") or message.startswith(
                "Anime") or message.startswith("70"):
      await self.highrise.send_emote("dance-anime", user.id)
      await self.highrise.chat(
          f" Tu me necesitas {user.username} y yo a ti igual😶‍🌫️")

    if message.startswith("/creepy") or message.startswith(
        "!creepy") or message.startswith("Creepy") or message.startswith("71"):
      await self.highrise.send_emote("dance-creepypuppet", user.id)
      await self.highrise.chat(
          f" Ashhh viejo sabroso {user.username} que ricooooo, okno😐")

    if message.startswith("/watch") or message.startswith(
        "!watch") or message.startswith("Watch") or message.startswith("72"):
      await self.highrise.send_emote("emote-creepycute", user.id)
      await self.highrise.chat(
          f" Envidioso de {user.username} jajaja dijiste q si ahora ya me puaf🥱"
      )

    if message.startswith("/revelations") or message.startswith(
        "!revelations") or message.startswith(
            "Revelations") or message.startswith("73"):
      await self.highrise.send_emote("emote-headblowup", user.id)
      await self.highrise.chat(
          f" Yo te vi volar {user.username} pero entre lo blanco mí, no podrás escapar ja😱"
      )

    if message.startswith("/bashful") or message.startswith(
        "!bashful") or message.startswith("Bashful") or message.startswith(
            "74"):
      await self.highrise.send_emote("emote-shy2", user.id)
      await self.highrise.chat(
          f" Oye mijo {user.username} me ayudas? tengo calzones alla traelos por favor🫤"
      )

    if message.startswith("/arabesque") or message.startswith(
        "!arabesque") or message.startswith("Arabesque") or message.startswith(
            "75"):
      await self.highrise.send_emote("emote-pose10", user.id)
      await self.highrise.chat(
          f" Te digo la verdad {user.username} te amo, pero a ti no😯"
      )

    if message.startswith("/party") or message.startswith(
        "!party") or message.startswith("Party") or message.startswith("76"):
      await self.highrise.send_emote("emote-celebrate", user.id)
      await self.highrise.chat(
          f" Fiesta Fiesta {user.username} Tumbala la casa mami🤣")

    if message.startswith("/skating") or message.startswith(
        "!skating") or message.startswith("Skating") or message.startswith(
            "77"):
      await self.highrise.send_emote("emote-iceskating", user.id)
      await self.highrise.chat(
          f" Lo caro tuyo {user.username} es pura ilusión tuya jajaja😮‍💨")

    if message.startswith("/scritchy") or message.startswith(
        "!scritchy") or message.startswith("Scritchy") or message.startswith(
            "78"):
      await self.highrise.send_emote("idle-wild", user.id)
      await self.highrise.chat(
          f" Controlate Sr. {user.username} no te calientes facil xd🤮")

    if message.startswith("/bitnervous") or message.startswith(
        "!bitnervous"
    ) or message.startswith("Bitnervous") or message.startswith(
        "!nervioso") or message.startswith("/nervioso") or message.startswith(
            "Nervioso") or message.startswith("79"):
      await self.highrise.send_emote("idle-nervous", user.id)
      await self.highrise.chat(
          f" Seria lo mas bueno que viste {user.username} pero alla tú😵‍💫")

    if message.startswith("/timejump") or message.startswith(
        "!timejump") or message.startswith("Timejump") or message.startswith(
            "80"):
      await self.highrise.send_emote("emote-timejump", user.id)
      await self.highrise.chat(
          f" Yo tengo Lamborghini y tú  {user.username} no tienes nada, pobreee😎"
      )

    if message.startswith("/gottago") or message.startswith(
        "!gottago") or message.startswith("Gottago") or message.startswith(
            "81"):
      await self.highrise.send_emote("idle-toilet", user.id)
      await self.highrise.chat(
          f" Pobre yo? Ah si? {user.username} Pues eso lo dices tu, mala vista envidiosa👽"
      )

    if message.startswith("/jingle") or message.startswith(
        "!jingle") or message.startswith("Jingle") or message.startswith("82"):
      await self.highrise.send_emote("dance-jinglebell", user.id)
      await self.highrise.chat(
          f" Te cojo gritas, te llamo vuelas {user.username} y ahora se enamora jdr😷"
      )

    if message.startswith("/hyped") or message.startswith(
        "!hyped") or message.startswith("Hyped") or message.startswith("83"):
      await self.highrise.send_emote("emote-hyped", user.id)
      await self.highrise.chat(
          f" Lo cokteario es El horario  {user.username} pero traelo y te meto el leonardo👻"
      )

    if message.startswith("/sleigh") or message.startswith(
        "!sleigh") or message.startswith("Sleigh") or message.startswith("84"):
      await self.highrise.send_emote("emote-sleigh", user.id)
      await self.highrise.chat(
          f" Se enamoró la niña {user.username} jajaja mira mira q feooo🤒")

    if message.startswith("/surprise") or message.startswith(
        "!surprise") or message.startswith("Surprise") or message.startswith(
            "85"):
      await self.highrise.send_emote("emote-pose6", user.id)
      await self.highrise.chat(
          f" WTF eh {user.username} Porque me envias fotos de klo. Que bueno y feo jaja☠️"
      )

    if message.startswith("/repose") or message.startswith(
        "!repose") or message.startswith("Repose") or message.startswith("86"):
      await self.highrise.send_emote("sit-relaxed", user.id)
      await self.highrise.chat(
          f" Te amo {user.username} hoy te pongo a prueba para ver si es mayor🌝"
      )

    if message.startswith("/kawaii") or message.startswith(
        "!kawaii") or message.startswith("Kawaii") or message.startswith("87"):
      await self.highrise.send_emote("dance-kawai", user.id)

    if message.startswith("/touch") or message.startswith(
        "!touch") or message.startswith("Touch") or message.startswith("88"):
      await self.highrise.send_emote("dance-touch", user.id)

    if message.startswith("/gift") or message.startswith(
        "!gift") or message.startswith("Gift") or message.startswith("89"):
      await self.highrise.send_emote("emote-gift", user.id)

    if message.startswith("/pushit") or message.startswith(
        "!pushit") or message.startswith("Pushit") or message.startswith("90"):
      await self.highrise.send_emote("dance-employee", user.id)

    if message.startswith("salute") or message.startswith(
        "!salute") or message.startswith("Salute") or message.startswith("91"):
      await self.highrise.send_emote("emote-cutesalute", user.id)

    if message.startswith("/attention") or message.startswith(
        "!attention") or message.startswith("Attention") or message.startswith(
            "92"):
      await self.highrise.send_emote("emote-salute", user.id)

    if message.startswith("/tiktok") or message.startswith(
        "!tiktok") or message.startswith("Tiktok") or message.startswith("93"):
      await self.highrise.send_emote("dance-tiktok11", user.id)

    if message.startswith("/smooch") or message.startswith(
        "!smooch") or message.startswith("Smooch") or message.startswith("94"):
      await self.highrise.send_emote("emote-kissing-bound", user.id)

    if message.startswith("/launch") or message.startswith(
        "!launch") or message.startswith("Launch") or message.startswith("95"):
      await self.highrise.send_emote("emote-launch", user.id)

    if message.startswith("Launch All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-launch", roomUser.id)

    if message.startswith("Smooch All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-kissing-bound", roomUser.id)

    if message.startswith("Pushit All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-employee", roomUser.id)

    if message.startswith("Gift All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-gift", roomUser.id)

    if message.startswith("Attention All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-salute", roomUser.id)

    if message.startswith("Salute All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-cutesalute", roomUser.id)

    if message.startswith("Tiktok All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-tiktok11", roomUser.id)

    if message.startswith("Touch All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-touch", roomUser.id)

    if message.startswith("Kawaii All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-kawai", roomUser.id)

    if message.startswith("Hot All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-hot", roomUser.id)

    if message.startswith("Curtsy All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-curtsy", roomUser.id)

    if message.startswith("Surprise All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose6", roomUser.id)

    if message.startswith("Jingle All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-jinglebell", roomUser.id)

    if message.startswith("Creepy All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-creepypuppet", roomUser.id)

    if message.startswith("Bitnervous All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-nervous", roomUser.id)

    if message.startswith("Scritchy All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-wild", roomUser.id)

    if message.startswith("Fashion All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-fashionista", roomUser.id)

    if message.startswith("Wrong All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-wrong", roomUser.id)

    if message.startswith("Cutey All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-cutey", roomUser.id)

    if message.startswith("Hyped All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-hyped", roomUser.id)

    if message.startswith("Superpose All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-superpose", roomUser.id)

    if message.startswith("Punk All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-punkguitar", roomUser.id)

    if message.startswith("Tiktok2 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-tiktok2", roomUser.id)

    if message.startswith("Savage All") or message.startswith("Tiktok8 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-tiktok8", roomUser.id)

    if message.startswith("Tiktok10 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-tiktok10", roomUser.id)

    if message.startswith("Viral All") or message.startswith(
        "Viralgroove All") or message.startswith("Tiktok9 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-tiktok9", roomUser.id)

    if message.startswith("Blackpink All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-blackpink", roomUser.id)
    if message.startswith("Gagging All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emoji-gagging", roomUser.id)

    if message.startswith("Pose3 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose3", roomUser.id)

    if message.startswith("Pose7 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose7", roomUser.id)

    if message.startswith("Pose5 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose5", roomUser.id)

    if message.startswith("Pose1 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose1", roomUser.id)

    if message.startswith("Pose8 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose8", roomUser.id)

    if message.startswith("Enthused All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-enthusiastic", roomUser.id)

    if message.startswith("Sing All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle_singing", roomUser.id)

    if message.startswith("Teleport All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-teleporting", roomUser.id)

    if message.startswith("Telekinesis All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-telekinesis", roomUser.id)

    if message.startswith("Casual All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-dance-casual", roomUser.id)

    if message.startswith("Icecream All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-icecream", roomUser.id)

    if message.startswith("Zombie All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-zombierun", roomUser.id)

    if message.startswith("Celebrate All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emoji-celebrate", roomUser.id)

    if message.startswith("Kiss All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-kiss", roomUser.id)

    if message.startswith("Snowangel All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-snowangel", roomUser.id)

    if message.startswith("Bow All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-bow", roomUser.id)

    if message.startswith("Skating All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-iceskating", roomUser.id)

    if message.startswith("Confused All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-confused", roomUser.id)

    if message.startswith("Charging All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-charging", roomUser.id)

    if message.startswith("Wei All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-weird", roomUser.id)

    if message.startswith("Greedy All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-greedy", roomUser.id)

    if message.startswith("Cursing All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emoji-cursing", roomUser.id)

    if message.startswith("Russian All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-russian", roomUser.id)

    if message.startswith("Repose All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("sit-relaxed", roomUser.id)

    if message.startswith("Shop All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-shoppingcart", roomUser.id)

    if message.startswith("Ren All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-macarena", roomUser.id)

    if message.startswith("Snake All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-snake", roomUser.id)

    if message.startswith("Model All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-model", roomUser.id)

    if message.startswith("Sleigh All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-sleigh", roomUser.id)

    if message.startswith("Tiktok4 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

    if message.startswith("Uwu All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-uwu", roomUser.id)

    if message.startswith("Star All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-stargazer", roomUser.id)

    if message.startswith("Pose9 All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose9", roomUser.id)

    if message.startswith("Boxer All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-boxer", roomUser.id)

    if message.startswith("Guitar All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-guitar", roomUser.id)

    if message.startswith("Penguin All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-pinguin", roomUser.id)

    if message.startswith("Zero All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-astronaut", roomUser.id)

    if message.startswith("aa"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("dance-anime", roomUser.id)

    if message.startswith("bb"):
      if user.username == "aex_savage_":
      roomUsers = (await self.highrise.get_room_users()).content
      for roomUser, _ in roomUsers:
        await self.highrise.send_emote("emote-lust", roomUser.id)

    if message.startswith("Watch All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-creepycute", roomUser.id)

    if message.startswith("Revelation All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-headblowup", roomUser.id)

    if message.startswith("Bashful All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-shy2", roomUser.id)

    if message.startswith("Arabesque All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-pose10", roomUser.id)

    if message.startswith("Party All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-celebrate", roomUser.id)

    if message.startswith("Time All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("emote-timejump", roomUser.id)

    if message.startswith("Gottago All"):
      if user.username == "aex_savage_":
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.send_emote("idle-toilet", roomUser.id)

    if message.startswith("bebidas"):
      await self.highrise.send_whisper(
          user.id, "esta es nuestra carta de bebidas, espero que os guste 😄")

    if message.startswith("bebidas"):
      await self.highrise.send_whisper(
          user.id,
          "tequila, ron, vino, vino blanco, vodka, whisky, ron, champagne, cachaça cognac, cerveza, cocacola, jugo, agua, aguadecoco, toddy, "
      )

    if message.startswith("coca cola"):
      await self.highrise.send_whisper(
          user.id,
          f"{user.username} aqui está su deliciosa coca cola helada 🧊🥤 ")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("toddy"):
      await self.highrise.send_whisper(
          user.id, f"{user.username} aqui está su delicioso toddy 🥛")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("jugo"):
      await self.highrise.send_whisper(
          user.id, f"{user.username} aqui está su delicioso jugo natural 🧃")
      await self.highrise.react("thumbs", user.id)
    if message.startswith("agua"):
      await self.highrise.send_whisper(
          user.id,
          f"🌊aqui está su deliciosa agua {user.username} diretamente de Ciego Montero🌊"
      )
      await self.highrise.react("thumbs", user.id)

    if message.startswith("agua de coco"):
      await self.highrise.send_whisper(
          user.id,
          f"🥥aqui está su agua de coco {user.username} aproveche que está deliciosa 🥥"
      )
      await self.highrise.react("thumbs", user.id)

    if message.startswith("nescau"):
      await self.highrise.send_whisper(
          user.id, f"aqui está {user.username} su delicioso nescau 🥛")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("tequila"):
      await self.highrise.send_whisper(
          user.id, f"{user.username} Disfrutando del Tequila 😄🥃")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("gin"):
      await self.highrise.send_whisper(
          user.id,
          f"dale la vuelta dale la vuelta a toda la ginebra {user.username} 🥃")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("coñac"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está Su coñac {user.username} 🥃🥃")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("whisky"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está su Whisky  {user.username} 🥃")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("ron"):
      await self.highrise.send_whisper(user.id,
                                       f"Aqui Está su Ron 🥃 {user.username}")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("cocuy"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está su Cocuy de Penca {user.username} 🍶")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("vodka"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está Su  Vodka {user.username} ")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("champaña"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está Su Champaña {user.username} 🍾🥂")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("cerveza"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está Su Cerveza {user.username} 🍺")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("vino blanco"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está Su Vino Blanco {user.username}")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("vino"):
      await self.highrise.send_whisper(user.id,
                                       f"Aqui Está Su Vino {user.username}")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("menu"):
      await self.highrise.send_whisper(
          user.id,
          "Este es nuestro menú de comidas y snacks, espero que os guste 😄")

    if message.startswith("menu"):
      await self.highrise.send_whisper(
          user.id,
          "camarones, ensalada de lechuga, ensalada de repollo, pasta, pizza, pastel de zanahoria"
      )

    if message.startswith("menu"):
      await self.highrise.send_whisper(
          user.id,
          "tarta de fresa, açai, helado, magdalena, papas fritas, kebab, pandeajo"
      )

    if message.startswith("pizza"):
      await self.highrise.send_whisper(
          user.id, f"{user.username} aqui está su deliciosa pizza 🍕")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("pastel de fresas"):
      await self.highrise.send_whisper(
          user.id,
          f"Aquí tienes tu Delicioso Pastel de Fresas {user.username} 🍰")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("ensalada de repollo"):
      await self.highrise.send_whisper(
          user.id,
          f"Aqui Está Su Deliciosa ensalada de repollo {user.username} 🥬🥬")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("camarones"):
      await self.highrise.send_whisper(
          user.id, f"🍤Aqui Están sus Delicosos Camarones 🍤 {user.username} 🍤")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("macarrones"):
      await self.highrise.send_whisper(
          user.id,
          f"Aqui Están sus macarrones {user.username} que aproveche 🍜🍝")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("ensalada de lechuga"):
      await self.highrise.send_whisper(
          user.id,
          f"Aquí está tu ensalada de lechuga {user.username} con un poco de tomates encima 🥬🥗"
      )
      await self.highrise.react("thumbs", user.id)

    if message.startswith("patel de zanahoria"):
      await self.highrise.send_whisper(
          user.id, f"aquí está tu pastel de zanahoria {user.username} 🥕🥮")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("porro"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Está Su porro {user.username} 🚬 Degustelo ")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("helado"):
      await self.highrise.send_whisper(
          user.id, f"Aquí está tu helado {user.username} 🍦🍨")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("pan de ajo"):
      await self.highrise.send_whisper(
          user.id, f"Aquí está tu pan de ajo {user.username} 🥖🧄")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("papas fritas"):
      await self.highrise.send_whisper(
          user.id, f"Aqui Están Sus papas Fritas {user.username} provecho 🍟")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("brocheta"):
      await self.highrise.send_whisper(
          user.id, f"Aquí está tu brocheta {user.username} 🍢🍢")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("tarta"):
      await self.highrise.send_whisper(
          user.id, f"Aquí está tu pastelito {user.username} 🧁")
      await self.highrise.react("thumbs", user.id)

    if message.startswith("/tp") or message.startswith(
        "!tp") or message.startswith("/tele") or message.startswith(
            "Tp") or message.startswith("Tele") or message.startswith("!tele"):
      target_username = message.split("@")[-1].strip()
      await self.teleport_to_user(user, target_username)

    if message.startswith("ven") or message.startswith(
        "/ven") or message.startswith("!ven"):
      if user.username == "aex_savage_":
        target_username = message.split("@")[-1].strip()
        await self.teleport_user_next_to(target_username, user)

    if message.startswith("kick"):
      if user.username == "aex_savage_":
        pass
      else:
        await self.highrise.chat(
            "No tienes permiso para utilizar este comando.")
        return
      #separete message into parts
      parts = message.split()
      #check if message is valid "kick @username"
      if len(parts) != 2:
        await self.highrise.chat("formato de baneo incorrecto.")
        return
      #checks if there's a @ in the message
      if "@" not in parts[1]:
        username = parts[1]
      else:
        username = parts[1][1:]
      #check if user is in room
      room_users = (await self.highrise.get_room_users()).content
      for room_user, pos in room_users:
        if room_user.username.lower() == username.lower():
          user_id = room_user.id
          break
      if "user_id" not in locals():
        await self.highrise.chat(
            "usuario no encontrado, arregle la coordenada del código")
        return
      #kick user
      try:
        await self.highrise.moderate_room(user_id, "kick")
      except Exception as e:
        await self.highrise.chat(f"{e}")
        return
      #send message to chat
      await self.highrise.chat(
          f"{username} ¡¡Le prohibieron la entrada a la sala!!")

  async def teleport(self, user: User, position: Position):
    try:
      await self.highrise.teleport(user.id, position)
    except Exception as e:
      print(f"Error de teletransporte detectado: {e}")

  async def teleport_to_user(self, user: User, target_username: str) -> None:
    try:
      room_users = await self.highrise.get_room_users()
      for target, position in room_users.content:
        if target.username.lower() == target_username.lower():
          z = position.z
          new_z = z - 1
          await self.teleport(
              user, Position(position.x, position.y, new_z, position.facing))
          break
    except Exception as e:
      print(
          f"Se produjo un error al teletransportarse a {target_username}: {e}")

  async def teleport_user_next_to(self, target_username: str,
                                  requester_user: User) -> None:
    try:
      # Get the position of the requester_user
      room_users = await self.highrise.get_room_users()
      requester_position = None
      for user, position in room_users.content:
        if user.id == requester_user.id:
          requester_position = position
          break

      # Find the target user and their position
      for user, position in room_users.content:
        if user.username.lower() == target_username.lower():
          z = requester_position.z
          new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
          await self.teleport(
              user,
              Position(requester_position.x, requester_position.y, new_z,
                       requester_position.facing))
          break
    except Exception as e:
      print(
          f"Se produjo un error al teletransportarse. {target_username} junto a {requester_user.username}: {e}"
      )

  async def teleporter(self, message: str) -> None:
    """
            Teletransporta al usuario o coordenada especificados.
            Usa: /teleport <username> <x,y,z>
                                                                """
    #separates the message into parts
    #part 1 is the command "/teleport"
    #part 2 is the name of the user to teleport to (if it exists)
    #part 3 is the coordinates to teleport to (if it exists)
    try:
      command, username, coordinate = message.split(" ")
    except:

      return

    #checks if the user is in the room
    room_users = (await self.highrise.get_room_users()).content
    for user in room_users:
      if user[0].username.lower() == username.lower():
        user_id = user[0].id
        break
    #if the user_id isn't defined, the user isn't in the room
    if "user_id" not in locals():

      return

    #checks if the coordinate is in the correct format (x,y,z)
    try:
      x, y, z = coordinate.split(",")
    except:

      return

    #teleports the user to the specified coordinate
    await self.highrise.teleport(user_id=user_id,
                                 dest=Position(float(x), float(y), float(z)))

  async def command_handler(self, user: User, message: str):
    parts = message.split(" ")
    command = parts[0][1:]
    functions_folder = "functions"
    # Check if the function exists in the module
    for file_name in os.listdir(functions_folder):
      if file_name.endswith(".py"):
        module_name = file_name[:-3]  # Remove the '.py' extension
        module_path = os.path.join(functions_folder, file_name)

        # Load the module
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Check if the function exists in the module
        if hasattr(module, command) and callable(getattr(module, command)):
          function = getattr(module, command)
          await function(self, user, message)

    # If no matching function is found
    return

  async def on_reaction(self, user: User, reaction: Reaction,
                        receiver: User) -> None:
    print(
        f"{user.username} envio una reaccion  {reaction} para {receiver.username}"
    )

    if reaction.startswith("wink"):
      await self.highrise.send_emote("idle-uwu", receiver.id)
      await self.highrise.send_emote("emote-lust", user.id)
      await self.highrise.send_emote("emote-ghost-idle")

    if reaction.startswith("heart"):
      await self.highrise.send_emote("emote-kissing-bound", receiver.id)
      await self.highrise.send_emote("emote-kissing-bound", user.id)
      await self.highrise.send_emote("emote-gordonshuffle")

    if reaction.startswith("wave"):
      await self.highrise.send_emote("emote-confused", receiver.id)
      await self.highrise.send_emote("emote-hello", user.id)
      await self.highrise.send_emote("dance-smoothwalk")

    if reaction.startswith("thumbs"):
      await self.highrise.send_emote("emote-pose1", receiver.id)
      await self.highrise.send_emote("dance-spiritual")

    if reaction.startswith("clap"):
      await self.highrise.send_emote("idle-enthusiastic", receiver.id)
      await self.highrise.send_emote("emoji-celebrate", user.id)
      await self.highrise.send_emote("dance-breakdance")

  async def on_whisper(self, user: User, message: str) -> None:
    print(f"{user.username} whispered: {message}")

    if message.startswith("/tele") or message.startswith(
        "/tp") or message.startswith("/fly") or message.startswith(
            "!tele") or message.startswith("!tp") or message.startswith(
                "!fly"):
      if user.username == "aex_savage_":
        await self.teleporter(message)

    if message.startswith("/") or message.startswith("!"):
      await self.command_handler(user, message)

    if message.startswith("/wallet") or message.startswith("!wallet"):
      if user.username == "aex_savage_":
        wallet = (await self.highrise.get_wallet()).content
        await self.highrise.send_whisper(
            user.id, f"VALOR TOTAL : {wallet[0].amount} {wallet[0].type}")
        await self.highrise.send_emote("emote-bunnyhop")

  async def on_user_move(self, user: User, pos: Position) -> None:
    print(f"{user.username} trasladado a {pos}")

  async def on_emote(self, user: User, emote_id: str,
                     receiver: User | None) -> None:
    print(f"{user.username} emoted: {emote_id}")

  async def on_user_leave(self, user: User) -> None:
    print(f"{user.username} salio de la sala")
    await self.highrise.chat(
        f"Se fue @{user.username}, ya vendran otros🔥"
    )
    await self.highrise.send_emote("dance-tiktok11")
