CREATE TABLE IF NOT EXISTS proprietario (
	pronome varchar(60) not null,
	procpf varchar(14) not null,
	primary key(procpf)
);

CREATE TABLE IF NOT EXISTS carro (
	carid integer not null,
	cartipo smallint not null,
	carcor smallint not null,
	procpf varchar(14) not null,
	primary key(carid),
	FOREIGN KEY (procpf) REFERENCES proprietario (procpf)
);

ALTER TABLE carro ADD CONSTRAINT ck_cor CHECK (carcor in (1, 2, 3));
ALTER TABLE carro ADD CONSTRAINT ck_tipo CHECK (cartipo in (1, 2, 3));


INSERT INTO proprietario (pronome, procpf) VALUES ('ADERBAL SILVA', '53815767067'), ('JANUARIO CLEITON MELO', '15245579006'), ('AGNALDO SILVRIO CRIMERIO TERCEITO', '35213743005');
INSERT INTO carro (carid, cartipo, carcor, procpf) VALUES (1, 3, 3, '53815767067'), (2, 2, 2, '53815767067'), (3, 1, 1, '53815767067');

