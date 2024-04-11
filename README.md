![Image](https://telegra.ph/file/f2750be308765b83b3937.jpg)

## 𝘈𝘯𝘪𝘮𝘦𝘏𝘞™ 


![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)<br> [![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)<br>
[![Support Group!](https://img.shields.io/badge/Join%20Group-↗-green)](https://t.me/collect_em_support)


_**Available On Telegram As 
[Collect Em all](https://t.me/Collect_em_AllBot) and**_
_Ask for Help in our [Support Chat](https://t.me/Collect_em_support)_

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

git clone https://github.com/<YourUsername>/WAIFU-HUSBANDO-CATCHER && cd WAIFU-HUSBANDO-CATCHER

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
