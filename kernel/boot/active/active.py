a
    7
a�  �                   @   s�   d dl Z ed� edd�Ze�� �d�Zed  sZed� e �d� edd�Ze�� �d�ZeD ].Ze	e�d d kr^ed� e �d� ed	� q^ed
� e �d� dS )�    Nu   检查系统激活z5/data/data/com.termux/files/home/.flyos/active/key.fk�r�-u;   序列号无效，可前往http://store.flyosgeek.com购买z'python $FLYOS/kernel/boot/active/buy.py�   u7   非FlyOS激活序列号，请检查或联系管理员!!u   正在启动zbash $FLYOS/munu.sh)
�os�print�open�f�read�split�i�system�_�int� r   r   �	active.py�<module>   s   




