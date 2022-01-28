${SegmentFile}

${SegmentPrePrimary}
	${If} ${FileExists} "$EXEDIR\Data\Config\plugins\config\*.*"
	${AndIfNot} ${FileExists} "$EXEDIR\Data\Config\plugins\config\nppPluginList.dll"
		CopyFiles /SILENT "$EXEDIR\App\DefaultData\Config\plugins\Config\nppPluginList.dll" "$EXEDIR\Data\Config\plugins\config"
	${EndIf}
!macroend
