# F-Drone Versão 0.0.1

[![GitHub stars](https://img.shields.io/github/stars/FinotiLucas/F-Drone)](https://github.com/FinotiLucas/F-Drone/stargazers) [![GitHub forks](https://img.shields.io/github/forks/FinotiLucas/F-Drone)](https://github.com/FinotiLucas/F-Drone/network)  [![GitHub license](https://img.shields.io/github/license/FinotiLucas/F-Drone)](https://github.com/FinotiLucas/F-Drone/blob/master/LICENSE)  [![GitHub issues](https://img.shields.io/github/issues/FinotiLucas/F-Drone)](https://github.com/FinotiLucas/F-Drone/issues) 


Date of Birth 03/06/2019  

Digital image processor for Drones, created with the motivation to be useful to the academic community and be an Open Source alternative to existing professional programs.  


# Funcionando:
- Planejamento de Vôo;
- Orientação Interior;
- Orientação Exterior;
- Aerotriangulação;
- Resseção Espacial.


# Sendo Implementado:
- Criação de Relatórios;
- Reorganizar os arquivos em Json;
- Colocar um simbolo no ponto escolhido na fotografia;
- Remover pontos escolhidos pelo usuário;
- Receber as Coordenadas de Pontos de controle;
- Exportar as coordenadas do planejamento de Voo para Shapefile;
- Ortofoto;
- Ortomosaico;
- MDT;
- MDS;
- Métodos Surf e Sift para coleta de pontos homologos.


## Instalação e Configuração

-----------

``` python
pip install -r requirements.txt

python FDrone.py
```
- OBS: (Crie um novo diretorio ao utilizar o FDrone, não use o diretório raiz como pasta de projeto)


## Fotos
![Interface](https://github.com/FinotiLucas/F-Drone/blob/master/ScreenShots/1.png?raw=true "Interface")

![Interface](https://github.com/FinotiLucas/F-Drone/blob/master/ScreenShots/2.png?raw=true "Interface")

![Interface](https://github.com/FinotiLucas/F-Drone/blob/master/ScreenShots/3.png?raw=true "Interface")


# Planejamento de Vôo

![Interface](https://github.com/FinotiLucas/F-Drone/blob/master/ScreenShots/4.png?raw=true "Interface")

# Exemplo de resultado:
![Interface](https://github.com/FinotiLucas/F-Drone/blob/master/ScreenShots/pv.png?raw=true "Interface")

# Exemplo de resultado em Json: 

``` json
{
    "Comprimento Longetudinal": 120,
    "Comprimento Transversal": 120,
    "Altura de Voo": 36,
    "Distancia Focal": 0.024,
    "Sobreposicao Longetudinal": 80,
    "Sobreposicao Lateral": 60,
    "Numero de Pixels Longetudinais": 3040,
    "Numero de Pixels Transversais": 4056,
    "GSD": 0.013,
    "Tempo de Exposicao": 0.002381,
    "Velocidade de Voo": 15,
    "Duracao da Bateria": 21,
    "Azimute de Voo": 285,
    "Azimute Transversal": 45,
    "Este": 635016.757,
    "Norte": 7481150.651,
    "\\u00c1rea": 14400,
    "Escala de voo": 0.0006666666666666666,
    "gsd": 0.000008666666666666666,
    "gl": 0.026346666666666664,
    "gt": 0.035151999999999996,
    "GL": 39.519999999999996,
    "GT": 52.727999999999994,
    "b": 0.005269333333333331,
    "B": 7.903999999999996,
    "Avan\\u00e7o da Base": 0.8,
    "w": 0.014060799999999998,
    "W": 21.0912,
    "\\u00c1rea do modelo Esteroscopico": 1667.0484479999998,
    "\\u00c1rea incremental de cada modelo Esteroscopico": 166.70484479999993,
    "N\\u00famero total de fotos em esteroscopia": 86,
    "Intervalo de eempo entre as exposi\\u00e7\\u00f5es": 0.13173333333333329,
    "N\\u00famero de fotos por faixa": 20,
    "N\\u00famero de Faixas": 7,
    "W Ajustado": 17.142857142857142,
    "N\\u00famero Total de Fotos": 140,
    "Dist\\u00e2ncia total percorrida pela aeronave": 1154.0891428571424,
    "Arrastamento Teorico": 0.000039683333333333333,
    "Tempo total de Voo": 76.93927619047616,
    "Dura\\u00e7\\u00e3o necessaria da Bateria": 6.106291761148902,
    "Coordenadas Este": "[635016.757, 635009.122322269, 635001.487644538, 634993.8529668071, 634986.2182890761, 634978.5836113452, 634970.9489336142, 634963.3142558832, 634955.6795781523, 634948.0449004213, 634940.4102226903, 634932.7755449594, 634925.1408672284, 634917.5061894974, 634909.8715117665, 634902.2368340355, 634894.6021563045, 634886.9674785736, 634879.3328008426, 634871.6981231116, 634883.8199536463, 634891.4546313772, 634899.0893091082, 634906.7239868392, 634914.3586645701, 634921.9933423011, 634929.6280200321, 634937.262697763, 634944.897375494, 634952.532053225, 634960.1667309559, 634967.8014086869, 634975.4360864179, 634983.0707641488, 634990.7054418798, 634998.3401196108, 635005.9747973417, 635013.6094750727, 635021.2441528037, 635028.8788305346, 635041.0006610693, 635033.3659833383, 635025.7313056074, 635018.0966278764, 635010.4619501454, 635002.8272724145, 634995.1925946835, 634987.5579169525, 634979.9232392216, 634972.2885614906, 634964.6538837596, 634957.0192060287, 634949.3845282977, 634941.7498505667, 634934.1151728358, 634926.4804951048, 634918.8458173738, 634911.2111396429, 634903.5764619119, 634895.9417841809, 634908.0636147156, 634915.6982924466, 634923.3329701775, 634930.9676479085, 634938.6023256395, 634946.2370033704, 634953.8716811014, 634961.5063588324, 634969.1410365633, 634976.7757142943, 634984.4103920253, 634992.0450697562, 634999.6797474872, 635007.3144252182, 635014.9491029491, 635022.5837806801, 635030.218458411, 635037.853136142, 635045.487813873, 635053.122491604, 635065.2443221386, 635057.6096444076, 635049.9749666767, 635042.3402889457, 635034.7056112147, 635027.0709334838, 635019.4362557528, 635011.8015780218, 635004.1669002909, 634996.5322225599, 634988.897544829, 634981.262867098, 634973.628189367, 634965.993511636, 634958.3588339051, 634950.7241561741, 634943.0894784431, 634935.4548007122, 634927.8201229812, 634920.1854452502, 634932.3072757849, 634939.9419535159, 634947.5766312468, 634955.2113089778, 634962.8459867088, 634970.4806644397, 634978.1153421707, 634985.7500199017, 634993.3846976326, 635001.0193753636, 635008.6540530946, 635016.2887308255, 635023.9234085565, 635031.5580862875, 635039.1927640184, 635046.8274417494, 635054.4621194804, 635062.0967972113, 635069.7314749423, 635077.3661526733, 635089.4879832079, 635081.853305477, 635074.218627746, 635066.583950015, 635058.949272284, 635051.3145945531, 635043.6799168221, 635036.0452390912, 635028.4105613602, 635020.7758836292, 635013.1412058983, 635005.5065281673, 634997.8718504363, 634990.2371727054, 634982.6024949744, 634974.9678172434, 634967.3331395125, 634959.6984617815, 634952.0637840505, 634944.4291063196]",
    "Coordenadas Norte": "[7481150.651, 7481152.6967057325, 7481154.742411465, 7481156.788117198, 7481158.833822931, 7481160.879528664, 7481162.925234397, 7481164.97094013, 7481167.016645863, 7481169.062351596, 7481171.1080573285, 7481173.153763061, 7481175.199468794, 7481177.245174527, 7481179.29088026, 7481181.336585993, 7481183.382291726, 7481185.427997459, 7481187.473703192, 7481189.5194089245, 7481201.641239459, 7481199.595533726, 7481197.549827993, 7481195.50412226, 7481193.458416527, 7481191.412710794, 7481189.367005061, 7481187.3212993285, 7481185.275593596, 7481183.229887863, 7481181.18418213, 7481179.138476397, 7481177.092770664, 7481175.047064931, 7481173.001359198, 7481170.955653465, 7481168.909947732, 7481166.864242, 7481164.818536267, 7481162.772830534, 7481174.894661068, 7481176.940366801, 7481178.986072534, 7481181.031778267, 7481183.077484, 7481185.123189732, 7481187.168895465, 7481189.214601198, 7481191.260306931, 7481193.306012664, 7481195.351718397, 7481197.39742413, 7481199.443129863, 7481201.488835596, 7481203.534541328, 7481205.580247061, 7481207.625952794, 7481209.671658527, 7481211.71736426, 7481213.763069993, 7481225.884900527, 7481223.839194794, 7481221.793489061, 7481219.747783328, 7481217.7020775955, 7481215.656371863, 7481213.61066613, 7481211.564960397, 7481209.519254664, 7481207.473548931, 7481205.427843198, 7481203.382137465, 7481201.336431732, 7481199.2907259995, 7481197.245020267, 7481195.199314534, 7481193.153608801, 7481191.107903068, 7481189.062197335, 7481187.016491602, 7481199.138322136, 7481201.184027869, 7481203.229733602, 7481205.275439335, 7481207.321145068, 7481209.366850801, 7481211.412556534, 7481213.458262267, 7481215.5039679995, 7481217.549673732, 7481219.595379465, 7481221.641085198, 7481223.686790931, 7481225.732496664, 7481227.778202397, 7481229.82390813, 7481231.869613863, 7481233.9153195955, 7481235.961025328, 7481238.006731061, 7481250.128561595, 7481248.082855863, 7481246.03715013, 7481243.991444397, 7481241.945738664, 7481239.900032931, 7481237.854327198, 7481235.808621465, 7481233.762915732, 7481231.717209999, 7481229.671504267, 7481227.625798534, 7481225.580092801, 7481223.534387068, 7481221.488681335, 7481219.442975602, 7481217.397269869, 7481215.351564136, 7481213.305858403, 7481211.260152671, 7481223.381983205, 7481225.427688938, 7481227.4733946705, 7481229.519100403, 7481231.564806136, 7481233.610511869, 7481235.656217602, 7481237.701923335, 7481239.747629068, 7481241.793334801, 7481243.839040534, 7481245.8847462665, 7481247.930451999, 7481249.976157732, 7481252.021863465, 7481254.067569198, 7481256.113274931, 7481258.158980664, 7481260.204686397, 7481262.25039213]"
}
``` 

### Development
----
Want to contribute? Great!
Sharing Code makes the world a better place <3


### Support
----

Help us to continue developing solutions for the community 

<center>
<a href="https://www.buymeacoffee.com/6cdltqC" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-blue.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>
</center>

# Bibliography

Bibliography: Introduction to Modern Photogrammetry of Edward M. Milkhail and James S. Bethel, J.Chris McGlone

### License
----

GNU Lesser General Public License v3.0

Copyright (c) 2020 Lucas Finoti.

[See more about the license][LICENSE]

