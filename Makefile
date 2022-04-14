# CLEAN
clean-ds-store:
	@echo "REMOVING all .DS_Store files"
	@rm -rfv .DS_Store & rm -rfv */.DS_Store & rm -rfv */*/.DS_Store & rm -rfv */*/*/.DS_Store & rm -rfv */*/*/*/.DS_Store

clean-server-dist:
	@rm -rfv server/dist/*

# INSTALL
install: clean-server-dist
	@mkdir -p ./server/dist/htdocs/v1
	@cp -rfv ./www/source/project/stable/ ./server/dist/htdocs/
	@cp -rfv ./www/source/project/v1/ ./server/dist/htdocs/v1
	@bash server/.bash install
