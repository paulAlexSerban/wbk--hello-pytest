# CLEAN
clean-ds-store:
	@echo "REMOVING all .DS_Store files"
	@rm -rfv .DS_Store & rm -rfv */.DS_Store & rm -rfv */*/.DS_Store & rm -rfv */*/*/.DS_Store & rm -rfv */*/*/*/.DS_Store

clean-server-dist:
	@rm -rfv server/dist/*

# INSTALL
install: clean-server-dist
	@mkdir -p ./server/dist/htdocs
	@bash server/.bash install

# RELEASE
release-site:
	@cp -rfv ./server/dist/htdocs/* ./docs