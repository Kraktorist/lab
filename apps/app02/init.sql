CREATE USER myUser;
CREATE DATABASE app;
GRANT ALL PRIVILEGES ON DATABASE app TO myUser;


\connect "app";

CREATE SEQUENCE status_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

BEGIN;
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
      NEW.updated = now(); 
      RETURN NEW;
END;
$$ language 'plpgsql';
COMMIT;

CREATE TABLE "public"."status" (
    "id" integer DEFAULT nextval('status_id_seq') NOT NULL,
    "name" text NOT NULL,
    "interval" integer NOT NULL,
    "updated" timestamp DEFAULT CURRENT_TIMESTAMP,
    "inserted" timestamp DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "status_name_key" UNIQUE ("name"),
    CONSTRAINT "status_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE TRIGGER "user_timestamp" BEFORE INSERT OR UPDATE ON "public"."status" FOR EACH ROW EXECUTE FUNCTION update_timestamp();;

