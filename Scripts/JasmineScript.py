import maya.cmds as cmds
expressionsJasmine = []
def defaultFaceAttributesJasmine():
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ",0)

	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl.tx",0)	
	   #endOfLipsTranslate
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tz",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tz",0)
	    
	    #tipBrowControlTranslate
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.tz",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.tz",0)
	
	    #middleBrowControlTranslate
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl.tz",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl.tz",0)
		
	  	#topEyeLidTranslate
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.tz",0)
	    
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.tz",0)
	    
	    #eyeBallTranslate
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl.tz",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl.tx",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl.ty",0)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl.tz",0)
	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.ty",0)			
	
	
def frownAttributesJasmine():
	defaultFaceAttributesJasmine() 
	#rearrange

	  
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.ty",-0.7)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tz",-0.002)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.ty",-0.7)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tz",-0.002)	    	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty",-1.5)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty",-1.5)		
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.ty",-1.354)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.ty",-1.354)	    
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl.ty",-16.347)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl.ty",-16.347)


def smileAttributesJasmine():
	defaultFaceAttributesJasmine()
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tx",-1.3674)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.ty",1.5034)	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tx",-1.3674)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.ty",1.5034)		
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty",0.7652)	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty",0.7652)
	
def happyAttributesJasmine():
	defaultFaceAttributesJasmine()

	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tx",-0.9)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.ty",1.5034)	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tx",-0.9)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.ty",1.5034)		
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty",0.7652)	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty",0.7652)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.ty",-2)	
	
		
def surpriseAttributesJasmine():
	defaultFaceAttributesJasmine()
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty",0.7652)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty",0.7652)		
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.ty",1.164)	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.ty",1.164)	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.ty",-2)		
	
def paranoiaAttributesJasmine():
	defaultFaceAttributesJasmine()


	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl.ty",-1)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_1_Ctrl.ty",-1)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl.tx",-51.598)	
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tx",1.5)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tx",1.5)
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.ty",-1)			
	
	
	
def disgustAttributesJasmine():
	defaultFaceAttributesJasmine()
	cmds.setAttr("Dude_Rt_Brow_1_Ctrl.ty",-3.207)
	cmds.setAttr("Dude_Lt_Brow_1_Ctrl.ty",-3.207)
	cmds.setAttr("Dude_Rt_Brow_3_Ctrl.ty",1.062)
	cmds.setAttr("Dude_Lt_Brow_3_Ctrl.ty",1.062)	
	
	cmds.setAttr("Dude_Rt_Rye_UpLid_Mstr_Ctrl.ty",-1.039)	
	cmds.setAttr("Dude_Lt_Rye_UpLid_Mstr_Ctrl.ty",-1.039)	
	
	
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.tx",2.496)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.ty",-1.591)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.tx",2.496)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.ty",-1.591)	

	cmds.setAttr("Dude_Rt_UpLip_2_Ctrl.ty",0.572)	
	cmds.setAttr("Dude_Lt_UpLip_2_Ctrl.ty",0.572)	
	cmds.setAttr("Dude_Rt_LoLip_4_Ctrl.ty",0.789)	
	cmds.setAttr("Dude_Lt_LoLip_4_Ctrl.ty",0.789)	
	
def Disgust(*args):
	disgustAttributesJasmine()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RtBrowTy(LeftSide)', minValue=-3.207, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_1_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LtBrowTy(LeftSide)', minValue=-3.207, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_1_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='LtBrowTy(MiddleControl)', minValue=-3.8540, maxValue=1.062, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_3_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RtBrowTy(MiddleControl)', minValue=-3.8540, maxValue=1.062, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_3_Ctrl.ty'  )
	cmds.text( label='EyeLid And Eyeball', align='center', backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='TopEyeLid(LtEye)', minValue=-1.039, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Rye_UpLid_Mstr_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='TopEyeLid(RtEye)', minValue=-1.039, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Rye_UpLid_Mstr_Ctrl.ty'  )	
	
		
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTx', minValue=-3.5, maxValue=2.496, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_UpLip_2_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTy', minValue=-1.591, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_UpLip_2_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTx', minValue=-3.5, maxValue=2.496, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTy', minValue=-1.591, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.ty'  )
	
	cmds.attrFieldSliderGrp(label='UpperLipControl2_Rt', minValue=-3.5, maxValue=0.572, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='UpperLipControl2_Lt', minValue=-1.591, maxValue=0.572, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LowerLipControl2_Rt', minValue=-3.5, maxValue=0.789, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_LoLip_4_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LowerLipControl2_Lt', minValue=-1.591, maxValue=0.789, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_LoLip_4_Ctrl.ty'  )	
	cmds.showWindow(window)	









def SmileJasmine(*args):
	smileAttributesJasmine()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ'  )


	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='LtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty')
	cmds.attrFieldSliderGrp(label='RtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty'  )
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.ty'  )
	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global JasminesliderSmile
	JasminesliderSmile=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)

	
	
		#tamam keda bygbly el values ba3d ma etghyrt
	def animateSmile(*args):
		global JasmineLtBrowTySmile,JasmineRtBrowTySmile,JasmineRightSideOfMouthTXSmile,JasmineRightSideOfMouthTYSmile,JasmineLeftSideOfMouthTXSmile,JasmineLeftSideOfMouthTYSmile
		JasmineLtBrowTySmile = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTySmile =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.translateY')
		JasmineRightSideOfMouthTXSmile = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateX')
		JasmineRightSideOfMouthTYSmile =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateY')
		JasmineLeftSideOfMouthTXSmile =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateX')
		JasmineLeftSideOfMouthTYSmile= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateY')
		defaultFaceAttributesJasmine()
	

	#rearrange
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0 ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=0,v=0  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
		
										#after
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=20,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=20,v=JasmineLeftSideOfMouthTXSmile  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=JasmineLeftSideOfMouthTYSmile)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=20,v= JasmineRightSideOfMouthTXSmile ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=20,v=JasmineRightSideOfMouthTYSmile )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineLtBrowTySmile  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineRtBrowTySmile  )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0	
		
			
		for x in range(21):
				cmds.currentTime( x, edit=True )
				
	def addExpression(*args):
		global jasmineNeckXSmile, jasmineNeckYSmile, jasmineNeckZSmile,JasmineLtBrowTySmile,JasmineRtBrowTySmile,JasmineRightSideOfMouthTXSmile,JasmineRightSideOfMouthTYSmile,JasmineLeftSideOfMouthTXSmile,JasmineLeftSideOfMouthTYSmile
		
		
		jasmineNeckXSmile = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX')
		jasmineNeckYSmile =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY')
		jasmineNeckZSmile = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ')
		
		
		JasmineLtBrowTySmile = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTySmile =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.translateY')
		JasmineRightSideOfMouthTXSmile = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateX')
		JasmineRightSideOfMouthTYSmile =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateY')
		JasmineLeftSideOfMouthTXSmile =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateX')
		JasmineLeftSideOfMouthTYSmile= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateY')
		JasminesliderSmileValue=cmds.intSliderGrp( JasminesliderSmile,q=True,value=True)
		for x in range(JasminesliderSmileValue+1):
			lastIndex=len(expressionsJasmine)-1	
			
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=jasmineNeckXSmile )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=jasmineNeckYSmile ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=jasmineNeckZSmile   )#5ALEHA 0 
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=JasmineLeftSideOfMouthTXSmile  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JasmineLeftSideOfMouthTYSmile)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 ) 
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v= JasmineRightSideOfMouthTXSmile ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRightSideOfMouthTYSmile )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 )  
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineLtBrowTySmile  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRtBrowTySmile  )#5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0) #5ALEHA 0	
		
			expressionsJasmine.append("smile")
			
			
			
	cmds.button(label='Animate', command=animateSmile,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))
		
	cmds.showWindow(window)
		
def HappyJasmine(*args):
	happyAttributesJasmine()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ'  )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='LtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty'  )
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.ty'  )
	cmds.text( label='Jaw', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='BottomJawTy', minValue=-5.681, maxValue=0, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.ty'  )
	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global JasminesliderHappy
	JasminesliderHappy=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)

	def animateHappy(*args):
		global JasmineLtBrowTyHappy,JasmineRtBrowTyHappy,JasmineRightSideOfMouthTXHappy,JasmineRightSideOfMouthTYHappy,JasmineLeftSideOfMouthTXHappy,JasmineLeftSideOfMouthTYHappy,JasmineJawControlTyHappy
		JasmineLtBrowTyHappy = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTyHappy =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.translateY')
		JasmineRightSideOfMouthTXHappy = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateX')
		JasmineRightSideOfMouthTYHappy =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateY')
		JasmineLeftSideOfMouthTXHappy =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateX')
		JasmineLeftSideOfMouthTYHappy= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateY')
		JasmineJawControlTyHappy= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.translateY')
		defaultFaceAttributesJasmine()
		
		
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0 ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=0,v=0  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
		
										#after
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=20,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=20,v=JasmineLeftSideOfMouthTXHappy   ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=JasmineLeftSideOfMouthTYHappy )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=20,v= JasmineRightSideOfMouthTXHappy  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=20,v=JasmineRightSideOfMouthTYHappy  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineLtBrowTyHappy ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineRtBrowTyHappy  )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=20,v=JasmineJawControlTyHappy ) #5ALEHA 0	
		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		global jasmineNeckXHappy,jasmineNeckYHappy ,jasmineNeckZHappy , JasmineLtBrowTyHappy,JasmineRtBrowTyHappy,JasmineRightSideOfMouthTXHappy,JasmineRightSideOfMouthTYHappy,JasmineLeftSideOfMouthTXHappy,JasmineLeftSideOfMouthTYHappy,JasmineJawControlTyHappy

		jasmineNeckXHappy = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX')
		jasmineNeckYHappy =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY')
		jasmineNeckZHappy = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ')



		JasmineLtBrowTyHappy = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTyHappy =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.translateY')
		JasmineRightSideOfMouthTXHappy = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateX')
		JasmineRightSideOfMouthTYHappy =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateY')
		JasmineLeftSideOfMouthTXHappy =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateX')
		JasmineLeftSideOfMouthTYHappy= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateY')
		JasmineJawControlTyHappy= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.translateY')
		JasminesliderHappyValue=cmds.intSliderGrp( JasminesliderHappy,q=True,value=True)
		for x in range(JasminesliderHappyValue + 1):
			lastIndex=len(expressionsJasmine)-1
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=jasmineNeckXHappy )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=jasmineNeckYHappy ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=jasmineNeckZHappy   )#5ALEHA 0 

			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=JasmineLeftSideOfMouthTXHappy   ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JasmineLeftSideOfMouthTYHappy )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 ) 
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v= JasmineRightSideOfMouthTXHappy  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRightSideOfMouthTYHappy  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 )  
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineLtBrowTyHappy ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRtBrowTyHappy  )#5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineJawControlTyHappy ) #5ALEHA 0	
			expressionsJasmine.append("happy")
		
		
	cmds.button(label='Animate', command=animateHappy,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))		
	cmds.showWindow(window)
	


def ParanoiaJasmine(*args):
	paranoiaAttributesJasmine()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='RtBrowTy(LeftSide)', minValue=-4.604, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_1_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LtBrowTy(LeftSide)', minValue=-4.604, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_1_Ctrl.ty'  )
	cmds.text( label='EyeBalls', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Both EyeBalls', minValue=-51.598, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_MainEyeAim_Ctrl.tx'  )
		
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTX', minValue=-3.5, maxValue=4.975, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTX', minValue=-3.5, maxValue=4.975, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.tx'  )

	cmds.text( label='Jaw', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='JawTy', minValue=-2.664, maxValue=0, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Jaw_Ctrl.ty'  )	
	
	def animateParanoia(*args):
		global LtBrowTyParanoia,RtBrowTyParanoia,BothEyesParanoia,RightSideOfMouthTXParanoia,LeftSideOfMouthTXParanoia,JawControlTyParanoia
		LtBrowTyParanoia = cmds.getAttr('Dude_Lt_Brow_1_Ctrl.translateY')
		RtBrowTyParanoia =  cmds.getAttr('Dude_Rt_Brow_1_Ctrl.translateY')
		BothEyesParanoia =  cmds.getAttr('Dude_MainEyeAim_Ctrl.translateX')
		RightSideOfMouthTXParanoia= cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateX')
		LeftSideOfMouthTXParanoia =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateX')

		JawControlTyParanoia= cmds.getAttr('Dude_Jaw_Ctrl.translateY')
		defaultFaceAttributesJasmine()
		
		
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=0,v=0 )#5ALEHA 0 
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=0 )#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=0 ) #5ALEHA 0
		
	
		
		#rearrange
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=20, v=BothEyesParanoia)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=20, v=RtBrowTyParanoia ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=20, v=LtBrowTyParanoia )#5ALEHA 0 
		
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20,v=LeftSideOfMouthTXParanoia ) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=RightSideOfMouthTXParanoia) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=20 ,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=20 ,v=0)#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=20,v=JawControlTyParanoia ) #5ALEHA 0
		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		global LtBrowTyParanoia,RtBrowTyParanoia,BothEyesParanoia,RightSideOfMouthTXParanoia,LeftSideOfMouthTXParanoia,JawControlTyParanoia
		LtBrowTyParanoia = cmds.getAttr('Dude_Lt_Brow_1_Ctrl.translateY')
		RtBrowTyParanoia =  cmds.getAttr('Dude_Rt_Brow_1_Ctrl.translateY')
		BothEyesParanoia =  cmds.getAttr('Dude_MainEyeAim_Ctrl.translateX')
		RightSideOfMouthTXParanoia= cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateX')
		LeftSideOfMouthTXParanoia =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateX')
		JawControlTyParanoia= cmds.getAttr('Dude_Jaw_Ctrl.translateY')
		expressions.append("paranoia")
		
		
	cmds.button(label='Animate', command=animateParanoia,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))	
	cmds.showWindow(window)






def FrownJasmine(*args):
	frownAttributesJasmine()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ'  )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='LtBrowTy(MiddleControl)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RtBrowTy(MiddleControl)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.ty'  )
	cmds.text( label='EyeLid And Eyeball', align='center', backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='TopEyeLid(LtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='TopEyeLid(RtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='EyeBall(LtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='EyeBall(RtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl.ty'  )	
		
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTZ', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.tz'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.tz'  )
	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global JasmineFrownSlider
	JasmineFrownSlider=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)
	def animateFrown(*args):
		global JasmineLtBrowTyFrown, JasmineRtBrowTyFrown, JasmineRt_Rye_UpLidFrown, JasmineLt_Rye_UpLidFrown, JasmineRt_EyeAim_CtrlFrown, JasmineLt_EyeAim_CtrlFrown, JasmineRightSideOfMouthTYFrown,JasmineRightSideOfMouthTZFrown,JasmineLeftSideOfMouthTYFrown,JasmineLeftSideOfMouthTZFrown
		JasmineLtBrowTyFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTyFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRt_Rye_UpLidFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.translateY')
		JasmineLt_Rye_UpLidFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.translateY')
		JasmineRt_EyeAim_CtrlFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl.translateY')
		JasmineLt_EyeAim_CtrlFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl.translateY')
		JasmineRightSideOfMouthTYFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateY')
		JasmineRightSideOfMouthTZFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateZ')
		JasmineLeftSideOfMouthTYFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateY')
		JasmineLeftSideOfMouthTZFrown= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateZ')
		defaultFaceAttributesJasmine()
		
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0 ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=0,v=0  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
		
										#after
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=20,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=20,v=0   ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=JasmineLeftSideOfMouthTYFrown  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=JasmineLeftSideOfMouthTZFrown  ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=20,v= 0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=20,v=JasmineRightSideOfMouthTYFrown   )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=JasmineRightSideOfMouthTZFrown  )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineLtBrowTyFrown  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineRtBrowTyFrown   )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=JasmineLt_Rye_UpLidFrown )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=JasmineRt_Rye_UpLidFrown )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=20,v=JasmineLt_EyeAim_CtrlFrown  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=20,v=JasmineRt_EyeAim_CtrlFrown  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0	

		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		global	jasmineNeckXFrown,jasmineNeckYFrown ,jasmineNeckZFrown,  JasmineLtBrowTyFrown, JasmineRtBrowTyFrown, JasmineRt_Rye_UpLidFrown, JasmineLt_Rye_UpLidFrown, JasmineRt_EyeAim_CtrlFrown, JasmineLt_EyeAim_CtrlFrown, JasmineRightSideOfMouthTYFrown,JasmineRightSideOfMouthTZFrown,JasmineLeftSideOfMouthTYFrown,JasmineLeftSideOfMouthTZFrown
	
	
		jasmineNeckXFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX')
		jasmineNeckYFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY')
		jasmineNeckZFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ')

	
	
		JasmineLtBrowTyFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTyFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRt_Rye_UpLidFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.translateY')
		JasmineLt_Rye_UpLidFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.translateY')
		JasmineRt_EyeAim_CtrlFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl.translateY')
		JasmineLt_EyeAim_CtrlFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl.translateY')
		JasmineRightSideOfMouthTYFrown = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateY')
		JasmineRightSideOfMouthTZFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl.translateZ')
		JasmineLeftSideOfMouthTYFrown =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateY')
		JasmineLeftSideOfMouthTZFrown= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl.translateZ')
		
		JasmineFrownSliderValue=cmds.intSliderGrp( JasmineFrownSlider,q=True,value=True)
		for x in range(JasmineFrownSliderValue+1):
			lastIndex=len(expressionsJasmine)-1
			
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=jasmineNeckXFrown )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=jasmineNeckYFrown ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=jasmineNeckZFrown   )#5ALEHA 0 

			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0   ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JasmineLeftSideOfMouthTYFrown  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=JasmineLeftSideOfMouthTZFrown  ) 
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v= 0  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRightSideOfMouthTYFrown   )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=JasmineRightSideOfMouthTZFrown  )  
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineLtBrowTyFrown  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRtBrowTyFrown   )#5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JasmineLt_Rye_UpLidFrown )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JasmineRt_Rye_UpLidFrown )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineLt_EyeAim_CtrlFrown  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRt_EyeAim_CtrlFrown  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 ) #5ALEHA 0
			expressionsJasmine.append("frown")
	cmds.button(label='Animate', command=animateFrown,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))	
	cmds.showWindow(window)


def SurpriseJasmine(*args):
	surpriseAttributesJasmine()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ'  )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='RtBrowTy(MiddleMuscle)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LtBrowTy(MiddleMuscle)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.ty'  )
	cmds.text( label='EyeLid', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RtTopEyeLid', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LtTopEyeLid', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.ty'  )
		
	cmds.text( label='Jaw', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='BottomJawTy', minValue=-5.681, maxValue=0, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.ty'  )

	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global JasmineSurpriseSlider
	JasmineSurpriseSlider=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)
	
	def animateSurprise(*args):
		global jasmineNeckXSurprise,jasmineNeckYSurprise ,jasmineNeckZSurprise, JasmineLtBrowTySurprise,JasmineRtBrowTySurprise,JasmineRt_Rye_UpLidSurprise,JasmineLt_Rye_UpLidSurprise,JasmineJawControlTySurprise
	
		jasmineNeckXSurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX')
		jasmineNeckYSurprise =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY')
		jasmineNeckZSurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ')

		JasmineLtBrowTySurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTySurprise =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.translateY')
		JasmineRt_Rye_UpLidSurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.translateY')
		JasmineLt_Rye_UpLidSurprise =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.translateY')
		JasmineJawControlTySurprise= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.translateY')
		defaultFaceAttributesJasmine()
		
		
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0 ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=0,v=0  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0  )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
	
		
		#rearrange
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=0 ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 ) 
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=20,v=0  ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=20,v=0  )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 )  
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineLtBrowTySurprise    ) #5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=20,v=JasmineRtBrowTySurprise    )#5ALEHA 0
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=JasmineLt_Rye_UpLidSurprise )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=JasmineRt_Rye_UpLidSurprise )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=20,v=JasmineJawControlTySurprise ) #5ALEHA 0
	
		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		global jasmineNeckXSurprise,jasmineNeckYSurprise ,jasmineNeckZSurprise,  JasmineLtBrowTySurprise,JasmineRtBrowTySurprise,JasmineRt_Rye_UpLidSurprise,JasmineLt_Rye_UpLidSurprise,JasmineJawControlTySurprise
		jasmineNeckXSurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateX')
		jasmineNeckYSurprise =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateY')
		jasmineNeckZSurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1.rotateZ')

	
		JasmineLtBrowTySurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl.translateY')
		JasmineRtBrowTySurprise =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl.translateY')
		JasmineRt_Rye_UpLidSurprise = cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl.translateY')
		JasmineLt_Rye_UpLidSurprise =  cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl.translateY')
		JasmineJawControlTySurprise= cmds.getAttr('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.translateY')
		
		JasmineSurpriseSliderValue=cmds.intSliderGrp( JasmineSurpriseSlider,q=True,value=True)
		for x in range(JasmineSurpriseSliderValue+1):
			lastIndex=len(expressionsJasmine)-1
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=jasmineNeckXSurprise )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=jasmineNeckYSurprise ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=jasmineNeckZSurprise   )#5ALEHA 0 

			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20 ,v=0 ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 ) 
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 )  
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineLtBrowTySurprise    ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineRtBrowTySurprise    )#5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JasmineLt_Rye_UpLidSurprise )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JasmineRt_Rye_UpLidSurprise )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=JasmineJawControlTySurprise ) #5ALEHA 0
			expressionsJasmine.append("surprise")
		
	cmds.button(label='Animate', command=animateSurprise,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))

	cmds.showWindow(window)

	





def TalkJasmine(*args):
	cmds.setAttr("JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl.ty",-2)		
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='How many seconds do you want her to talk?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global talkTimeJasmine
	talkTimeJasmine=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)
	def addExpression(*args):
		talkTimeValueJasmine=cmds.intSliderGrp( talkTimeJasmine,q=True,value=True)
		for x in range(talkTimeValueJasmine):
			expressionsJasmine.append("talk")
	cmds.button(label='Add to Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))
	cmds.showWindow(window)






def Execute(*args):
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateX',time=0  ,v=0)
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateY',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateZ',time=0 ,v=0  )#5ALEHA 0 
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=0 ,v=0)
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_1_Ctrl' ,attribute='translateY',time=0 ,v=0 )#5ALEHA 0 
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0)
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 ) 
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0)
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 )  
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=0,v=0 )#5ALEHA 0
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=0,v=0)
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=0,v=0 )
	cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
	for i, x in enumerate(expressionsJasmine):

		if x =="talk":
			
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateX',time=(i+1) *20  ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateY',time=(i+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateZ',time=(i+1) *20 ,v=0  )#5ALEHA 0 
			
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,attribute='translateX',time=(i+1) *20,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateX',time=(i+1) *20,v=0   ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,attribute='translateZ',time=(i+1) *20,v=0  ) 
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateX',time=(i+1) *20,v= 0  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0   )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,attribute='translateZ',time=(i+1) *20,v=0  )  
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0  ) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0   )#5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0 )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0  )
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 ) #5ALEHA 0	
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateX',time=(i+1) *20  ,v=0)
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateY',time=(i+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1' ,attribute='rotateZ',time=(i+1) *20 ,v=0  )#5ALEHA 0 
			
			


		
		if x=="paranoia":
			cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=(i+1) *20, v=BothEyesParanoia)
			cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=(i+1) *20, v=RtBrowTyParanoia ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=(i+1) *20, v=LtBrowTyParanoia )#5ALEHA 0 
			
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(i+1) *20,v=LeftSideOfMouthTXParanoia ) #5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(i+1) *20,v=0 ) 
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(i+1) *20 ,v=RightSideOfMouthTXParanoia) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(i+1) *20,v=0 )  
			cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)#5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=(i+1) *20,v=JawControlTyParanoia ) #5ALEHA 0


def ResetExpressionQueueJasmine(*args):
	global expressionsJasmine
	expressionsJasmine=[]
	cmds.cutKey('JasmineRose_Rig_V_1:JasmineRose_Neck_FK_Ctrl_1','JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Mouth_Lt_Crnr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Mouth_Rt_Crnr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_2_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Rt_Brow_Main_2_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Lt_Brow_Main_1_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Lt_UpEye_Mstr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Rt_UpEye_Mstr_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl' ,'JasmineRose_Rig_V_1:JasmineRose_Jaw_Ctrl' ,cl=True, time=(0,10000))
def resetFaceJasmine(*args):
	defaultFaceAttributesJasmine()
	



#msh beysave el values ama adoos add facial expression i guess? fa adeef el global variable declaration bardo fee add expression?
# run el code b animate el awel then save exp

def startAnimation(*args):
	cmds.currentTime(0)
	cmds.play( forward=True,sound="convo2" )



cmds.window(width=300,t="Jasmine Facial Expressions")
cmds.columnLayout(adjustableColumn=True)
cmds.button(label='Smile', command=SmileJasmine,backgroundColor=(0.0,0.0,0.1))
cmds.button(label='Frown', command=FrownJasmine,backgroundColor=(0.0,0.3,0.1))
cmds.button(label='Surprise', command=SurpriseJasmine, backgroundColor=(0.0,0.0,0.5))
cmds.button(label='Happy', command=HappyJasmine, backgroundColor=(0.0,0.5,0.5))
#cmds.button(label='Paranoia', command=ParanoiaJasmine, backgroundColor=(0.5,0.5,1))
cmds.button(label='Idle', command=TalkJasmine, backgroundColor=(0.5,0.5,1))

#cmds.button(label='Disgust', command=Disgust, backgroundColor=(0.5,0.5,0))
cmds.button(label='Add All Expressions', command=Execute, backgroundColor=(0.5,0.5,0.5))
cmds.button(label='Reset facial expressions', command=ResetExpressionQueueJasmine, backgroundColor=(1,0.5,0.5))
cmds.button(label='Start Animation', command=startAnimation, backgroundColor=(0.5,1,0.5))

cmds.button(label='Default Face', command=resetFaceJasmine)


cmds.showWindow()