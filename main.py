import datetime

data_namoro = datetime.datetime(2025, 2, 8, 20, 0, 0)

html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>❤️ João & Victória ❤️</title>
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background-color: white;
      font-family: 'Arial', sans-serif;
      text-align: center;
      overflow: hidden;
    }}

    h1 {{
      margin-top: 20px;
      font-size: 6vw;
      color: #b30000;
    }}

    .timer {{
      font-size: 5vw;
      color: #800000;
    }}

    img {{
      margin-top: 20px;
      max-width: 80%;
      height: auto;
      border-radius: 20px;
      border: 4px solid #b30000;
      box-shadow: 0 0 20px rgba(179, 0, 0, 0.3);
    }}

    audio {{
      margin-top: 20px;
      width: 80%;
    }}

    .heart {{
      position: absolute;
      color: red;
      font-size: 24px;
      animation: float 5s infinite ease-in-out;
    }}

    @keyframes float {{
      0% {{
        transform: translateY(100vh) scale(1);
        opacity: 1;
      }}
      100% {{
        transform: translateY(-10vh) scale(0.5);
        opacity: 0;
      }}
    }}
  </style>
</head>
<body>

  <h1>João Henrique & Victória Campos</h1>

  <div class="timer" id="contador"></div>

  <img src="foto-casal.jpeg" alt="Foto do casal">

  <audio controls autoplay loop>
    <source src="musica-romantica.mp3" type="audio/mpeg">
    Seu navegador não suporta áudio.
  </audio>

  <script>
    function criarCoracao() {{
      const coracao = document.createElement("div");
      coracao.classList.add("heart");
      coracao.style.left = Math.random() * 100 + "vw";
      coracao.style.animationDuration = (2 + Math.random() * 3) + "s";
      coracao.innerText = "❤️";
      document.body.appendChild(coracao);
      setTimeout(() => coracao.remove(), 5000);
    }}
    setInterval(criarCoracao, 300);
  </script>

  <script>
    const inicio = new Date("{data_namoro.strftime("%Y-%m-%dT%H:%M:%S")}").getTime();

    function atualizarContador() {{
      const agora = new Date().getTime();
      const diferenca = agora - inicio;

      const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));
      const horas = Math.floor((diferenca / (1000 * 60 * 60)) % 24);
      const minutos = Math.floor((diferenca / (1000 * 60)) % 60);
      const segundos = Math.floor((diferenca / 1000) % 60);

      document.getElementById("contador").innerText =
        `${{dias}} dias, ${{horas}}h ${{minutos}}m ${{segundos}}s`;
    }}

    setInterval(atualizarContador, 1000);
    atualizarContador();
  </script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Site responsivo vermelho e branco gerado com sucesso!")
