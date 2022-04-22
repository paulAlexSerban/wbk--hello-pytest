## CLEAN
clean-ds-store:
	@echo "REMOVING all .DS_Store files"
	@rm -rfv .DS_Store & rm -rfv */.DS_Store & rm -rfv */*/.DS_Store & rm -rfv */*/*/.DS_Store & rm -rfv */*/*/*/.DS_Store

clean-docs:
	@rm -rfv docs/*

## INSTALL
install-npm-dependencies:
	@npm install --prefix assets && npm install --prefix frontend

## DEPLOY SCRIPTS
deploy-assets:
	@npm run deploy --prefix assets

deploy-frontend:
	@npm run deploy --prefix frontend

deploy-all: clean-docs
	@make deploy-assets && make deploy-frontend

## DOCKER INSTANCE SCRIPTS
build-compose-container:
	@docker-compose --env-file .env up --build --detach

stop-and-remove-all-compose-projects: clean-ds-store
	@docker-compose down --volumes --rmi all

## WATCHERS
start-frontend-watches:
	npm run watch --prefix frontend