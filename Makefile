# CLEAN
clean-ds-store:
	@echo "REMOVING all .DS_Store files"
	@rm -rfv .DS_Store & rm -rfv */.DS_Store & rm -rfv */*/.DS_Store & rm -rfv */*/*/.DS_Store & rm -rfv */*/*/*/.DS_Store

build-compose-container:
	@docker-compose --env-file .env up --build --detach

start-compose-container:
	@docker-compose --env-file .env up --detach

stop-all-compose-projects: clean-ds-store
	@docker-compose down --volumes --rmi all