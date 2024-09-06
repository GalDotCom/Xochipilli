import discord
import random
intents = discord.Intents.default()
intents.reactions = True



class LetterBot(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.letter_lists = {
            "1️⃣": ['https://youtu.be/umAGi80FsPM?si=MQE0VT17mOIFjxIv', 'https://youtu.be/5kBMHvvWlcs?si=rbQRpT7RR9Mu2_2d', 'https://youtu.be/H7gw87sZJxY?si=xzwFOPgVC5kYrYAD', 'https://youtu.be/ICmBpFdHIMc?si=yLiyBbY94RNypsfk', 'https://youtu.be/j3p36rzeoq8?si=w-aT57Wwsc7yWSxx'],
            "2️⃣": ['https://youtu.be/lnI0Py1dPkg?si=h0SIaCZZQLaebm-F', 'https://youtu.be/G3Vlm8abEfc?si=ErSpx5PsrfFRX_pm', 'https://youtu.be/FhzK5Eq7c7c?si=hkpQTsDnew97R2ki', 'https://youtu.be/5q2HSdgO7CA?si=tKHC1Qg7TdWu1tjP', 'https://youtu.be/WOR0ytnVuB4?si=BhaEZ_3eJSYUm5f9'],
            "3️⃣": ['https://youtu.be/v81H59mOMcQ?si=oaN1Hmqc0q7Q7s5H', 'https://youtu.be/YE33M1Xb0to?si=_91BHk9Uq0FucW_W', 'https://youtu.be/SpJhOTTG6X4?si=RnmbsHiLkLf3Askr', 'https://youtu.be/khMCFg64ALs?si=IBzZQrAM1GepwWS5', 'https://youtu.be/D_u6mNlHprE?si=jacDYxKF0-9SZMiH'],
            "4️⃣": ['https://youtu.be/nQcXm9rmdZM?si=gL3foTzbKv0Bw4yS', 'https://youtu.be/2kk7K7nIwCg?si=jedUi-zJZZsGLSQx', 'https://youtu.be/mKqd7gfWuig?si=qkF-i8JneuHSFeYA', 'https://youtu.be/x8gofrL8CXA?si=vHuQTuK0CSy-dWJp', 'https://youtu.be/3B2GVkeyF_Y?si=QlNIiImxvBhP8_SV']
        }

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Comando para enviar el mensaje y agregar reacciones
        if message.content == "$react":
            msg = await message.channel.send("Reacciona con un emoji para obtener informacion de ciertos temas de reciclaje, 1️⃣ para calentamiento global, 2️⃣ de reciclaje, 3️⃣ ideas de reciclaje y 4️⃣ energias limpias:")
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")

    async def on_reaction_add(self, reaction, user):
        if user == self.user:
            return

        if str(reaction.emoji) in self.letter_lists:
            chosen_list = self.letter_lists[str(reaction.emoji)]
            random_letter = random.choice(chosen_list)
            await reaction.message.channel.send(f"{user.mention}, has reaccionado con {reaction.emoji}. Aquí tienes un video: {random_letter}")

client = LetterBot(intents=intents)
intents.reactions = True

client.run("token")
