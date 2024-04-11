![Image](https://telegra.ph/file/631a7065550ff1fc949b5.jpg)

## 𝘈𝘯𝘪𝘮𝘦𝘏𝘞™ 


[![ADM Suporte](https://img.shields.io/badge/ADM-Suporte-blue.svg?style=flat-square)](https://t.me/Bielzin_nx)<br>  [![Grupo Oficial](https://img.shields.io/badge/Grupo-Oficial-blue.svg?style=flat-square)](https://t.me/Animesbetsbando)<br>
[![Shadizinho Criador!](https://img.shields.io/badge/Shadizinho%20Criador-↗-blue)](https://t.me/Shadizinho)


_**Disponível no Telegram como 
[𝘈𝘯𝘪𝘮𝘦𝘏𝘞™](https://t.me/AnimeHW_bot) e**_
_Peça ajuda em nosso [Grupo Oficial](https://t.me/Animesbetsbando)_

## 𝘚𝘰𝘣𝘳𝘦 𝘰 𝘙𝘦𝘱𝘰𝘴𝘪𝘵ó𝘳𝘪𝘰
● Esta é uma implementação de código aberto do AnimeHW™ para Telegram
- Por exemplo, Grab/Hunt/Protecc/Collect etc.. Esses tipos de bot Você deve ter visto em seus grupos de telegramas..
- Este bot envia caracteres em grupo a cada 100 mensagens de grupos. Então qualquer usuário pode adivinhar o nome desse personagem usando o comando /guess.

- Agora você também pode implantar esse tipo de bot. Usando nossa fonte, usamos Python-Telegram-Bot V20.6 e também lil bit Pyrogram. Aproveitar!

## 𝘊𝘖𝘔𝘖 𝘊𝘈𝘙𝘙𝘌𝘎𝘈𝘙 𝘗𝘌𝘙𝘚𝘖𝘕𝘈𝘎𝘌𝘕𝘚?

Formatar:
```
/upload img_url nome do personagem nome do anime número de raridade
```
#### Exemplo:
```
/upload Img_url muzan-kibutsuji Matador de Demônios 3
```



use o número de raridade de acordo com o mapa de raridade

| Number | Rarity     |
| ------ | -----------|
| 1 | ⚪️ Common   |
| 2 | 🟣 Rare     |
| 3 | 🟡 Legendary|
| 4 | 🟢 Medium   |

![Image](https://telegra.ph/file/9fcd8de2b174cec5f70d1.jpg)

## COMANDOS DO USUÁRIO
- `/guess` - Adivinhe o personagem
- `/fav` - Adicione um personagem aos favoritos
- `/trade` - Troca um personagem com outro usuário
- `/gift` - Presenteie um personagem para outro usuário
- `/collection` - Ostente sua coleção de harém
- `/topgroups` - Lista os grupos com maior harém (globalmente)
- `/top` - Lista os usuários com maior harém (globalmente)
- `/ctop` - Lista os usuários com maior harém (chat atual)
- `/changetime` - Altera a frequência de geração de personagens
  
## COMANDOS DO USUÁRIO SUDO..
- `/upload` - Adiciona um novo caracter ao banco de dados
- `/delete` - Exclui um caractere do banco de dados
- `/update` - Atualizar estatísticas de um personagem no banco de dados 

## COMANDOS DO PROPRIETÁRIO
- `/ping` - Faz ping no bot e envia uma resposta
- `/stats` - Lista números ou grupos e usuários
- `/list` - Envia um documento com a lista de todos os usuários que usaram o bot
- `/groups` - Envia um documento com a lista de todos os grupos em que o bot esteve

## MÉTODOS DE IMPLEMENTAÇÃO

### Heroku
- Fork o repositório
- Vá para [`config.py`](./shivu/config.py)
- Preencha todas as variáveis ​​e vá para heroku. e implante seu repositório bifurcado

### Implantação local/VPS
- Preencha variáveis ​​em [`config.py`](./shivu/config.py)
- Abra seu terminal VPS (estamos usando Debian) e execute o seguinte:
```bash
sudo apt-get update && sudo apt-get upgrade -y           

sudo apt-get install python3-pip -y          
sudo pip3 install -U pip

git clone https://github.com/<nomedeusuario>/WAIFU-HUSBANDO-CATCHER && cd WAIFU-HUSBANDO-CATCHER

pip3 install -U -r requirements.txt          

sudo apt install tmux && tmux          
python3 -m shivu
```       
 
## Licença
A fonte é licenciada pelo MIT e, portanto, não possui nenhuma garantia.

## Apreciação
Se você aprecia este Código, marque com estrela ✨ o repositório.

## Sugestões do desenvolvedor
- Não use heroku. Implantar no Heroku é apenas para teste. Caso contrário, o Inline do Bot funcionará muito devagar.
- Use um provedor VPS confiável
