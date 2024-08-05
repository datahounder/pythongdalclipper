import json
from osgeo import gdal

gdal.UseExceptions()
gdal.SetConfigOption('CPL_DEBUG', 'ON')

# ---------------------- Error warping 

# polygon follows the right-hand rule
#geometry_rh = {"type":"Polygon","coordinates":[[[27.007844753475,50.64392603116],[27.007845,50.643926],[27.005943,50.642279],[27.005662,50.64194],[27.006151,50.640338],[27.006098,50.639968],[27.005745,50.638644],[27.004111,50.635882],[27.00408,50.63524],[27.004112,50.635139],[27.004313,50.635078],[27.009981,50.634396],[27.010084,50.634588],[27.009928,50.636236],[27.010012,50.636476],[27.011096,50.637894],[27.012878,50.63932],[27.013014,50.639619],[27.012794,50.640079],[27.012539,50.640943],[27.011756,50.641385],[27.011731,50.641511],[27.011804,50.641644],[27.012096,50.641956],[27.012189,50.642173],[27.012115,50.643212],[27.012013,50.643399],[27.011916160985,50.643411244338],[27.011953678651,50.643531215779],[27.011938281604,50.643557889209],[27.011926729532,50.643586033517],[27.01191704598,50.643614815952],[27.011912241115,50.643630163105],[27.011909671501,50.643644685918],[27.011910521824,50.643661314022],[27.011911481062,50.643677101511],[27.011912404349,50.643693700242],[27.011913059849,50.643710369232],[27.011914533102,50.643728734323],[27.011915631329,50.643746839107],[27.011917704457,50.643764022435],[27.011919363858,50.643780300227],[27.01192252046,50.643797234057],[27.01192622893,50.643813283563],[27.011931065201,50.64382871891],[27.011937526997,50.643844810795],[27.011942771133,50.643859959582],[27.011948156126,50.643876724322],[27.011950462898,50.643894289248],[27.011950440176,50.643911009315],[27.011951237877,50.643927426405],[27.011953463808,50.643944171536],[27.011955785323,50.643959974601],[27.011959978204,50.643976327703],[27.011962772094,50.64399187908],[27.01196433732,50.644009107218],[27.011961101352,50.644025713753],[27.011947893544,50.644053789863],[27.011898940906,50.644112997404],[27.011864500349,50.644160372614],[27.011836828281,50.644170847591],[27.011798995771,50.644178642141],[27.011753150698,50.644184982941],[27.011708094036,50.644191240615],[27.011670128192,50.644196379691],[27.011634480594,50.644202994791],[27.011601024495,50.644207971342],[27.011566302087,50.644213310817],[27.011528910572,50.644223117275],[27.011494218956,50.644233614526],[27.011464254659,50.644243364064],[27.011435402011,50.644258229228],[27.011406324481,50.64426760111],[27.011373187032,50.644282170974],[27.011342127866,50.644295089048],[27.011313307885,50.644310044776],[27.011286021671,50.644322934811],[27.011241278781,50.644347843492],[27.01121781055,50.644359876586],[27.011176814183,50.644382883863],[27.011137190694,50.644408517589],[27.011116901985,50.644418246225],[27.011075289562,50.644444777042],[27.01103401029,50.644468564055],[27.011012926685,50.644478171657],[27.010992040506,50.644488455753],[27.01095060238,50.64451304081],[27.010906662427,50.644540924745],[27.010883891002,50.644552307768],[27.010840232563,50.64457710885],[27.010817259739,50.644588525345],[27.010795133633,50.644597596748],[27.010751064845,50.644622677788],[27.010707908073,50.644649196458],[27.010683442159,50.644661126307],[27.010659433262,50.644672770094],[27.010633725152,50.644684975396],[27.010608360577,50.644695757908],[27.010585788832,50.64470461896],[27.010541349112,50.644727374175],[27.010500903635,50.644753544581],[27.010457543249,50.644778179114],[27.010436289524,50.644788205888],[27.010412985816,50.644798998288],[27.010394362249,50.644804186737],[27.010370815241,50.644816803593],[27.010327453346,50.644846012759],[27.010305475514,50.644855604798],[27.010284344821,50.644865083296],[27.01024051049,50.64489061533],[27.010215691552,50.644904870427],[27.010188907691,50.644919160234],[27.010163625757,50.644933180912],[27.010120335582,50.64495786319],[27.010101880528,50.64496539615],[27.010041532606,50.645007331934],[27.010010164105,50.645025690287],[27.009943016727,50.64507998546],[27.009889488832,50.645123280847],[27.009837390403,50.645160947294],[27.009806851919,50.645174712721],[27.009688882943,50.645276397006],[27.00966720588,50.645285333629],[27.009644276392,50.645294703837],[27.009622829517,50.645300448592],[27.009599380019,50.64530480536],[27.00958136774,50.645306574499],[27.00956057757,50.645309134217],[27.009539687881,50.645310145958],[27.009519662191,50.645309564614],[27.009501606791,50.645308767843],[27.009482340655,50.64530724874],[27.009465450649,50.645304000975],[27.009450929607,50.645299894686],[27.009439285675,50.645296445643],[27.009425356398,50.645293218508],[27.009410562783,50.645288697905],[27.009395690784,50.645285243748],[27.009380265236,50.64528165987],[27.009361638572,50.645276288313],[27.009347553528,50.645269387551],[27.009331724551,50.645260203707],[27.009323959885,50.645252100735],[27.009313621441,50.645243825644],[27.009301920083,50.645234779127],[27.009291019427,50.645225438052],[27.009279948595,50.645215755431],[27.009269414491,50.645206969526],[27.009257274193,50.645197958364],[27.009247020125,50.645189097138],[27.009237568937,50.645179642853],[27.009228917912,50.64517024729],[27.009218049807,50.645160092558],[27.009206981547,50.645149228],[27.009196053936,50.645138137438],[27.009184144743,50.645126126147],[27.009171911915,50.645113688813],[27.00916077743,50.645101502433],[27.009150719896,50.645091100363],[27.009140507825,50.645082024665],[27.009131784335,50.645074108845],[27.008058707192,50.644146649757],[27.008048173439,50.644137781185],[27.008041446253,50.644130551593],[27.008027389106,50.644120410995],[27.008019464336,50.644113711216],[27.008004061052,50.644104262731],[27.007988628375,50.644092701107],[27.007977103917,50.644080398091],[27.007961860517,50.644067310648],[27.007948838597,50.644054883483],[27.007939646585,50.644044655558],[27.007933865656,50.644036721349],[27.007922035422,50.644026380775],[27.007909966147,50.644014399035],[27.007896132344,50.643999689122],[27.007890246849,50.643993875321],[27.007880718366,50.643984734532],[27.007869170499,50.643974675134],[27.007862876968,50.643967691827],[27.007855691189,50.643961006694],[27.007844753475,50.64392603116]]]}

# save the cutline to a temporary file


# crop image to cutline - results in error
#s = gdal.Warp('', '/vsicurl/http://landsat-pds.s3.amazonaws.com/c1/L8/183/025/LC08_L1TP_183025_20190602_20190602_01_RT/LC08_L1TP_183025_20190602_20190602_01_RT_B5.TIF', options=' -of MEM -r near  -ot Float32 -tr 30.000000000000 30.000000000000 -cutline /tmp/geom.geojson -crop_to_cutline -wo CUTLINE_ALL_TOUCHED=TRUE -srcnodata 0.000000000000 -dstnodata 0.000000000000')

# ---------------------- Successful warping 

# this is the same polygon, but now it does not follow the right-hand rule
#geometry_non_rh = {"type":"Polygon","coordinates": [list(reversed(geometry_rh["coordinates"][0]))]}

# save the cutline to a temporary file
#path_json = 'D:/map.geojson'
#with open(path_json, "w") as f:
#   f.write(json.dumps(geometry_non_rh))

# crop image to cutline - success
ds = gdal.Warp('', 'KM003320MI_010_MUL_L1T.tif', options=' -of MEM -r near  -ot Float32 -tr 30.000000000000 30.000000000000 -cutline map.geojson -crop_to_cutline -wo CUTLINE_ALL_TOUCHED=TRUE -srcnodata 0.000000000000 -dstnodata 0.000000000000')