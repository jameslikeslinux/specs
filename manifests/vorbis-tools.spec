# pkg:/vorbis-tools@1.2.0-1
set name=pkg.name            value="Vorbis Tools"
set name=description         value="Vorbis Audio Encoder and Utilities"
set name=pkg.description     value="vorbis-tools contains oggenc (an encoder) and ogg123 (a playback tool). It also has vorbiscomment (to add comments to Vorbis files), ogginfo (to give all useful information about an Ogg file, including streams in it), oggdec (a simple command line decoder), and vcut (which allows you to cut up Vorbis files)."
set name=info.maintainer     value="James Lee <jlee@thestaticvoid.org>"
set name=info.upsteram_url   value="http://www.vorbis.com/"
set name=info.source_url     value="http://downloads.xiph.org/releases/vorbis/vorbis-tools-1.2.0.tar.gz"
set name=info.classification value="org.opensolaris.category.2008:Applications/Sound and Video"

depend fmri=pkg:/SUNWcar type=require
depend fmri=pkg:/SUNWcs type=require
depend fmri=pkg:/SUNWcsd type=require
depend fmri=pkg:/SUNWcsl type=require
depend fmri=pkg:/SUNWkvm type=require
depend fmri=pkg:/SUNWflac type=require
depend fmri=pkg:/SUNWogg-vorbis type=require
depend fmri=pkg:/SUNWspeex type=require
depend fmri=pkg:/curl type=require
depend fmri=pkg:/libao type=require

legacy category=application desc="Vorbis Audio Encoder and Utilities" hotline="http://www.vorbis.com/" name="Vorbis Tools" pkg="vorbis-tools" vendor="http://downloads.xiph.org/releases/vorbis/vorbis-tools-1.2.0.tar.gz"
