# REBEL LLM PANEL

?? **REBEL LLM PANEL** ¡÷ Terminal tabanl?, gorev odakl?, *offline* cal??an LLM yonetim ve kontrol panelidir.

## Ozellikler
- YAML tabanl? gorev yonetimi
- Terminal GUI uzerinden gorev listesi goruntuleme, filtreleme
- Gorev detay gosterme
- Gorev komut cal??t?rma (subprocess)
- Log goruntuleme (son 20 sat?r)
- Dosya goruntuleme (log dosyalar? ve YAML)
- Gorev duzenleme h?zl? eri?im
- Snapshot alma (tasks.yaml yede?i)

## Kullan?m
```bash
git clone https://github.com/anillaksu/rebel-llm-panel.git
cd rebel-llm-panel
pip install -r requirements.txt
python main.py
Proje Yap?s?
bash
Kopyala
Duzenle
¢u¢w¢w core/           ¡÷ Ana moduller (logger, task runner, test runner, vb.)
¢u¢w¢w tasks/          ¡÷ Gorev listesi ve gorev ?ablonlar?
¢u¢w¢w ui/             ¡÷ Terminal GUI ve panel scriptleri
¢u¢w¢w logs/           ¡÷ Log dosyalar?
¢u¢w¢w scripts/        ¡÷ Kurulum ve destek scriptleri
¢u¢w¢w main.py         ¡÷ Ana giri? noktas? (REBEL LLM PANEL)
¢u¢w¢w requirements.txt
¢u¢w¢w README.md
¢|¢w¢w LICENSE
Gereksinimler
Python >= 3.9

Windows / Linux (test edilmi?)

Lisans
MIT License ¡÷ LICENSE dosyas?na bak?n?z.