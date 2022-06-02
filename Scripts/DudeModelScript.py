import maya.cmds as cmds


expressions = []
def defaultFaceAttributes():
	
	
	#neck control
	cmds.setAttr("Dude_Neck_Ctrl.rotateX",0)
	cmds.setAttr("Dude_Neck_Ctrl.rotateY",0)
	cmds.setAttr("Dude_Neck_Ctrl.rotateZ",0)

	
	cmds.setAttr("Dude_Rt_UpLip_2_Ctrl.ty",0)	
	cmds.setAttr("Dude_Lt_UpLip_2_Ctrl.ty",0)	
	cmds.setAttr("Dude_Rt_LoLip_4_Ctrl.ty",0)	
	cmds.setAttr("Dude_Lt_LoLip_4_Ctrl.ty",0)	
	
	
	
	cmds.setAttr("Dude_Lo_Mouth_Main_Ctrl.ty",0)	

	
	
	cmds.setAttr("Dude_MainEyeAim_Ctrl.tx",0)	
	cmds.setAttr("Dude_Rt_Brow_1_Ctrl.ty",0)
	cmds.setAttr("Dude_Lt_Brow_1_Ctrl.ty",0)  
	   #endOfLipsTranslate
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.tx",0)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.ty",0)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.tz",0)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.tx",0)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.ty",0)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.tz",0)
	    
	    #tipBrowControlTranslate
	cmds.setAttr("Dude_Lt_Brow_2_Ctrl.tx",0)
	cmds.setAttr("Dude_Lt_Brow_2_Ctrl.ty",0)
	cmds.setAttr("Dude_Lt_Brow_2_Ctrl.tz",0)
	cmds.setAttr("Dude_Rt_Brow_2_Ctrl.tx",0)
	cmds.setAttr("Dude_Rt_Brow_2_Ctrl.ty",0)
	cmds.setAttr("Dude_Rt_Brow_2_Ctrl.tz",0)
	
	    #middleBrowControlTranslate
	cmds.setAttr("Dude_Lt_Brow_3_Ctrl.tx",0)
	cmds.setAttr("Dude_Lt_Brow_3_Ctrl.ty",0)
	cmds.setAttr("Dude_Lt_Brow_3_Ctrl.tz",0)
	cmds.setAttr("Dude_Rt_Brow_3_Ctrl.tx",0)
	cmds.setAttr("Dude_Rt_Brow_3_Ctrl.ty",0)
	cmds.setAttr("Dude_Rt_Brow_3_Ctrl.tz",0)
		
	  	#topEyeLidTranslate
	cmds.setAttr("Dude_Lt_Rye_UpLid_Mstr_Ctrl.tx",0)
	cmds.setAttr("Dude_Lt_Rye_UpLid_Mstr_Ctrl.ty",0)
	cmds.setAttr("Dude_Lt_Rye_UpLid_Mstr_Ctrl.tz",0)
	    
	cmds.setAttr("Dude_Rt_Rye_UpLid_Mstr_Ctrl.tx",0)
	cmds.setAttr("Dude_Rt_Rye_UpLid_Mstr_Ctrl.ty",0)
	cmds.setAttr("Dude_Rt_Rye_UpLid_Mstr_Ctrl.tz",0)
	    
	    
	cmds.setAttr("Dude_Lt_Rye_LoLid_Mstr_Ctrl.tx",0)
	cmds.setAttr("Dude_Lt_Rye_LoLid_Mstr_Ctrl.ty",0)
	cmds.setAttr("Dude_Lt_Rye_LoLid_Mstr_Ctrl.tz",0)
	    
	cmds.setAttr("Dude_Rt_Rye_LoLid_Mstr_Ctrl.tx",0)
	cmds.setAttr("Dude_Rt_Rye_LoLid_Mstr_Ctrl.ty",0)
	cmds.setAttr("Dude_Rt_Rye_LoLid_Mstr_Ctrl.tz",0)
	    
	    
	    #eyeBallTranslate
	cmds.setAttr("Dude_Lt_EyeAim_Ctrl.tx",0)
	cmds.setAttr("Dude_Lt_EyeAim_Ctrl.ty",0)
	cmds.setAttr("Dude_Lt_EyeAim_Ctrl.tz",0)
	cmds.setAttr("Dude_Rt_EyeAim_Ctrl.tx",0)
	cmds.setAttr("Dude_Rt_EyeAim_Ctrl.ty",0)
	cmds.setAttr("Dude_Rt_EyeAim_Ctrl.tz",0)
	
	
	 #Jaw
	cmds.setAttr("Dude_Jaw_Ctrl.ty",0)			
	
	
def frownAttributes():
	defaultFaceAttributes() 
	#rearrange

	  
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.ty",-3.457)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.tz",-0.002)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.ty",-3.457)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.tz",-0.002)	    	
	cmds.setAttr("Dude_Lt_Brow_3_Ctrl.ty",-3.854)
	cmds.setAttr("Dude_Rt_Brow_3_Ctrl.ty",-3.854)		
	cmds.setAttr("Dude_Lt_Rye_UpLid_Mstr_Ctrl.ty",-1.354)
	cmds.setAttr("Dude_Rt_Rye_UpLid_Mstr_Ctrl.ty",-1.354)	    
	cmds.setAttr("Dude_Lt_EyeAim_Ctrl.ty",-16.347)
	cmds.setAttr("Dude_Rt_EyeAim_Ctrl.ty",-16.347)


def smileAttributes():
	defaultFaceAttributes()
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.tx",-1.735)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.ty",3.41)	
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.tx",-1.735)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.ty",3.41)		
	cmds.setAttr("Dude_Lt_Brow_2_Ctrl.ty",2.943559)	
	cmds.setAttr("Dude_Rt_Brow_2_Ctrl.ty",2.943559)

def angryAttributes():
	defaultFaceAttributes()
	cmds.setAttr("Dude_Lo_Mouth_Main_Ctrl.ty",-2.226)	
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.ty",-3.68)	
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.ty",-3.68)		
	cmds.setAttr("Dude_Lt_Brow_2_Ctrl.ty",-3.861)	
	cmds.setAttr("Dude_Rt_Brow_2_Ctrl.ty",-3.861)
	cmds.setAttr("Dude_Lt_Rye_LoLid_Mstr_Ctrl.ty",-1.767)
	cmds.setAttr("Dude_Rt_Rye_LoLid_Mstr_Ctrl.ty",-1.767)




def happyAttributes():
	defaultFaceAttributes()

	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.tx",-1.735)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.ty",3.41)	
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.tx",-1.735)
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.ty",3.41)		
	cmds.setAttr("Dude_Lt_Brow_2_Ctrl.ty",2.943559)	
	cmds.setAttr("Dude_Rt_Brow_2_Ctrl.ty",2.943559)
	cmds.setAttr("Dude_Jaw_Ctrl.ty",-5.681)	
	
		
def surpriseAttributes():
	defaultFaceAttributes()
	cmds.setAttr("Dude_Rt_Brow_3_Ctrl.ty",2.966)
	cmds.setAttr("Dude_Lt_Brow_3_Ctrl.ty",2.966)		
	cmds.setAttr("Dude_Rt_Rye_UpLid_Mstr_Ctrl.ty",1.164)	
	cmds.setAttr("Dude_Lt_Rye_UpLid_Mstr_Ctrl.ty",1.164)	
	cmds.setAttr("Dude_Jaw_Ctrl.ty",-5.681)		
	
def paranoiaAttributes():
	defaultFaceAttributes()


	cmds.setAttr("Dude_Rt_Brow_1_Ctrl.ty",-4.604)
	cmds.setAttr("Dude_Lt_Brow_1_Ctrl.ty",-4.604)
	cmds.setAttr("Dude_MainEyeAim_Ctrl.tx",-51.598)	
	cmds.setAttr("Dude_Rt_Mouth_Crnr_Ctrl.tx",4.975)
	cmds.setAttr("Dude_Lt_Mouth_Crnr_Ctrl.tx",4.975)
	cmds.setAttr("Dude_Jaw_Ctrl.ty",-2.664)			
	
	
	
def disgustAttributes():
	defaultFaceAttributes()
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
	disgustAttributes()
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

def Angry(*args):
	angryAttributes()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateZ'  )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='LtBrowTy', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_2_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RtBrowTy', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_2_Ctrl.ty'  )
	cmds.text( label='EyeLids', align='center', backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='BottomLtEyelid', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Rye_LoLid_Mstr_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='BottomRtEyelid', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Rye_LoLid_Mstr_Ctrl.ty'  )	
	
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='BottomMiddleLip', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lo_Mouth_Main_Ctrl.ty'  )

	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global sliderAngry
	sliderAngry=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)

	def animateAngry(*args):
		neckX= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckY= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZ= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')
		LtBrowTy = cmds.getAttr('Dude_Lt_Brow_2_Ctrl.translateY')
		RtBrowTy =  cmds.getAttr('Dude_Rt_Brow_2_Ctrl.translateY')
		Rt_Rye_LoLid= cmds.getAttr('Dude_Rt_Rye_LoLid_Mstr_Ctrl.translateY')
		Lt_Rye_LoLid =  cmds.getAttr('Dude_Lt_Rye_LoLid_Mstr_Ctrl.translateY')
		RightSideOfMouthTY = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTY =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		MiddleLipBottom =  cmds.getAttr('Dude_Lo_Mouth_Main_Ctrl.translateY')


		defaultFaceAttributes()
		cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=0 ,v=0)
		cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=0,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=0 ,v=0 )#5ALEHA 0 
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=0 )#5ALEHA 0 
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0, ) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0, )
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=0 ,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=0 ,v=0)#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=0 )		
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 )	
		cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=0 )	
		cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=0 )	
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=0 )	
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0	
			
	
		
		#rearrange
		cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=20,v=neckX)
		cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=20,v=neckY) #5ALEHA 0
		cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=20 ,v=neckZ )#5ALEHA 0 
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=20 ,v=0 )#5ALEHA 0 	
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=LeftSideOfMouthTY )
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20 ,v=0) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20,v=RightSideOfMouthTY  )
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20 ,v=0	)  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=20,v=LtBrowTy  ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=20,v=RtBrowTy  )#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=Lt_Rye_LoLid )
		cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=Rt_Rye_LoLid)	
		cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=20 ,v=MiddleLipBottom )
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0

		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		neckX= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckY= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZ= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')
		LtBrowTy = cmds.getAttr('Dude_Lt_Brow_2_Ctrl.translateY')
		RtBrowTy =  cmds.getAttr('Dude_Rt_Brow_2_Ctrl.translateY')
		Rt_Rye_LoLid= cmds.getAttr('Dude_Rt_Rye_LoLid_Mstr_Ctrl.translateY')
		Lt_Rye_LoLid =  cmds.getAttr('Dude_Lt_Rye_LoLid_Mstr_Ctrl.translateY')
		RightSideOfMouthTY = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTY =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		MiddleLipBottom =  cmds.getAttr('Dude_Lo_Mouth_Main_Ctrl.translateY')
		sliderAngryValue=cmds.intSliderGrp( sliderAngry,q=True,value=True)
		for x in range(sliderAngryValue+1):
			lastIndex=len(expressions)-1
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=neckX)
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=neckY) #5ALEHA 0
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=neckZ )#5ALEHA 0 
			cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )#5ALEHA 0 
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20  ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=LeftSideOfMouthTY  )
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20 ,v=0) 
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=RightSideOfMouthTY   )
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20 ,v=0)  
			cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=LtBrowTy  ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=RtBrowTy  )#5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )
			cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )
			cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=0)
			cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			
			cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=Lt_Rye_LoLid )
			cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=Rt_Rye_LoLid )	
			cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=MiddleLipBottom  )	

			cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			expressions.append("angry")
	cmds.button(label='Animate', command=animateAngry,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))	
	cmds.showWindow(window)






def Talk(*args):
	cmds.setAttr("Dude_Jaw_Ctrl.ty",-3)		
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='How many seconds do you want him to talk?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global talkTime
	talkTime=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)
	def addExpression(*args):
		talkTimeValue=cmds.intSliderGrp( talkTime,q=True,value=True)
		for x in range(talkTimeValue):
			expressions.append("talk")
	cmds.button(label='Add to Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))
	cmds.showWindow(window)
	
def Smile(*args):
	smileAttributes()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateZ'  )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='LtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_2_Ctrl.ty')
	cmds.attrFieldSliderGrp(label='RtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_2_Ctrl.ty'  )
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.ty'  )
	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global sliderSmile
	sliderSmile=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)
	
	
		#tamam keda bygbly el values ba3d ma etghyrt
	def animateSmile(*args):
		global LtBrowTySmile,RtBrowTySmile,RightSideOfMouthTXSmile,RightSideOfMouthTYSmile,LeftSideOfMouthTXSmile,LeftSideOfMouthTYSmile
		LtBrowTySmile = cmds.getAttr('Dude_Lt_Brow_2_Ctrl.translateY')
		RtBrowTySmile =  cmds.getAttr('Dude_Rt_Brow_2_Ctrl.translateY')
		RightSideOfMouthTXSmile = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateX')
		RightSideOfMouthTYSmile =  cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTXSmile =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateX')
		LeftSideOfMouthTYSmile= cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		
		defaultFaceAttributes()
	

	#rearrange
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=0 )#5ALEHA 0 
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=0 )#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
		
										#after
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=20 ,v=0 )#5ALEHA 0 
		
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=LeftSideOfMouthTXSmile) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=LeftSideOfMouthTYSmile)
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=RightSideOfMouthTXSmile) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=RightSideOfMouthTYSmile)
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=20 ,v=LtBrowTySmile) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=20,v=RtBrowTySmile )#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0		
		
			
		for x in range(21):
				cmds.currentTime( x, edit=True )
				
	def addExpression(*args):
		global neckXSmile ,neckYSmile ,neckZSmile ,LtBrowTySmile,RtBrowTySmile,RightSideOfMouthTXSmile,RightSideOfMouthTYSmile,LeftSideOfMouthTXSmile,LeftSideOfMouthTYSmile
		
		neckXSmile= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckYSmile= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZSmile= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')
		
		LtBrowTySmile = cmds.getAttr('Dude_Lt_Brow_2_Ctrl.translateY')
		RtBrowTySmile =  cmds.getAttr('Dude_Rt_Brow_2_Ctrl.translateY')
		RightSideOfMouthTXSmile = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateX')
		RightSideOfMouthTYSmile =  cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTXSmile =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateX')
		LeftSideOfMouthTYSmile= cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		sliderSmileValue=cmds.intSliderGrp( sliderSmile,q=True,value=True)
	

		for x in range(sliderSmileValue+1):
			
			lastIndex=len(expressions)-1
			
			cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )	
			cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )
			
			
			
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=neckXSmile)
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=neckYSmile) #5ALEHA 0
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=neckZSmile )#5ALEHA 0 

			cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20 ,v=0)
			cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )#5ALEHA 0 
			
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20 ,v=LeftSideOfMouthTXSmile) #5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=LeftSideOfMouthTYSmile)
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20,v=0 ) 
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20 ,v=RightSideOfMouthTXSmile) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=RightSideOfMouthTYSmile)
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20,v=0 )  
			cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=LtBrowTySmile) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=RtBrowTySmile )#5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=0 )
			cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0)
			cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0)
			cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=0 )
			cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=0 )
			cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=0 ) #5ALEHA 0
			expressions.append("smile")
	cmds.button(label='Animate', command=animateSmile,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))
		
	cmds.showWindow(window)
		
def Happy(*args):
	happyAttributes()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )

	cmds.text( label='Neck Control', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateZ'  )



	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='LtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_2_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RtBrowTy(RightSide)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_2_Ctrl.ty'  )
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTX', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.tx'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.ty'  )
	cmds.text( label='Jaw', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='BottomJawTy', minValue=-5.681, maxValue=0, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Jaw_Ctrl.ty'  )
	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global sliderHappy
	sliderHappy=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)
	
	def animateHappy(*args):
		global neckXHappy,neckYHappy,neckZHappy,LtBrowTyHappy,RtBrowTyHappy,RightSideOfMouthTXHappy,RightSideOfMouthTYHappy,LeftSideOfMouthTXHappy,LeftSideOfMouthTYHappy,JawControlTyHappy
		neckXHappy= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckYHappy= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZHappy= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')
		
		
		LtBrowTyHappy = cmds.getAttr('Dude_Lt_Brow_2_Ctrl.translateY')
		RtBrowTyHappy =  cmds.getAttr('Dude_Rt_Brow_2_Ctrl.translateY')
		RightSideOfMouthTXHappy = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateX')
		RightSideOfMouthTYHappy =  cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTXHappy =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateX')
		LeftSideOfMouthTYHappy= cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		JawControlTyHappy= cmds.getAttr('Dude_Jaw_Ctrl.translateY')
		defaultFaceAttributes()
		
		
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=0)#5ALEHA 0 
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
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=0,v=0 )
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=0 ) #5ALEHA 0
		
	
		
		#rearrange
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=20 ,v=0 )#5ALEHA 0 
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20,v=LeftSideOfMouthTXHappy ) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=LeftSideOfMouthTYHappy)
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=RightSideOfMouthTXHappy) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20,v=RightSideOfMouthTYHappy )
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=20 ,v=LtBrowTyHappy) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=20,v=RtBrowTyHappy )#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=20 ,v=JawControlTyHappy) #5ALEHA 0
		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		
		global neckXHappy,neckYHappy,neckZHappy,LtBrowTyHappy,RtBrowTyHappy,RightSideOfMouthTXHappy,RightSideOfMouthTYHappy,LeftSideOfMouthTXHappy,LeftSideOfMouthTYHappy,JawControlTyHappy
		neckXHappy= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckYHappy= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZHappy= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')
		
		
		LtBrowTyHappy = cmds.getAttr('Dude_Lt_Brow_2_Ctrl.translateY')
		RtBrowTyHappy =  cmds.getAttr('Dude_Rt_Brow_2_Ctrl.translateY')
		RightSideOfMouthTXHappy = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateX')
		RightSideOfMouthTYHappy =  cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTXHappy =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateX')
		LeftSideOfMouthTYHappy= cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		JawControlTyHappy= cmds.getAttr('Dude_Jaw_Ctrl.translateY')
		sliderHappyValue=cmds.intSliderGrp( sliderHappy,q=True,value=True)
		for x in range(sliderHappyValue+1):
			lastIndex=len(expressions)-1
			cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )	
			cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )
			
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=neckXHappy)
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=neckYHappy) #5ALEHA 0
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=neckZHappy  )#5ALEHA 0 
			
			
			
			
			cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )#5ALEHA 0 
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20 ,v=LeftSideOfMouthTXHappy ) #5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=LeftSideOfMouthTYHappy)
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20 ,v=0 ) 
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20  ,v=RightSideOfMouthTXHappy) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=RightSideOfMouthTYHappy )
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20 ,v=0 )  
			cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=LtBrowTyHappy) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=RtBrowTyHappy )#5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )
			cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )
			cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )
			cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=JawControlTyHappy) #5ALEHA 0			
			expressions.append("happy")
		
		
	cmds.button(label='Animate', command=animateHappy,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))		
	cmds.showWindow(window)
	


def Paranoia(*args):
	paranoiaAttributes()
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
		defaultFaceAttributes()
		
		
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






def Frown(*args):
	frownAttributes()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateZ'  )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='LtBrowTy(MiddleControl)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_3_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RtBrowTy(MiddleControl)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_3_Ctrl.ty'  )
	cmds.text( label='EyeLid And Eyeball', align='center', backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='TopEyeLid(LtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Rye_UpLid_Mstr_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='TopEyeLid(RtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Rye_UpLid_Mstr_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='EyeBall(LtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_EyeAim_Ctrl.ty'  )	
	cmds.attrFieldSliderGrp(label='EyeBall(RtEye)', minValue=-3.8540, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_EyeAim_Ctrl.ty'  )	
		
	cmds.text( label='Lips', align='center',backgroundColor=(0.0,0.0,0.1),height= 18)
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LeftSideOfMouthTZ', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Mouth_Crnr_Ctrl.tz'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='RightSideOfMouthTY', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Mouth_Crnr_Ctrl.tz'  )
		
	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global sliderFrown
	sliderFrown=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)

	def animateFrown(*args):
		global neckXFrown ,neckYFrown ,neckZFrown , LtBrowTyFrown, RtBrowTyFrown, Rt_Rye_UpLidFrown, Lt_Rye_UpLidFrown, Rt_EyeAim_CtrlFrown, Lt_EyeAim_CtrlFrown, RightSideOfMouthTYFrown,RightSideOfMouthTZFrown,LeftSideOfMouthTYFrown,LeftSideOfMouthTZFrown
		neckXFrown= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckYFrown= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZFrown= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')

	
		LtBrowTyFrown = cmds.getAttr('Dude_Lt_Brow_3_Ctrl.translateY')
		RtBrowTyFrown =  cmds.getAttr('Dude_Rt_Brow_3_Ctrl.translateY')
		Rt_Rye_UpLidFrown = cmds.getAttr('Dude_Rt_Rye_UpLid_Mstr_Ctrl.translateY')
		Lt_Rye_UpLidFrown =  cmds.getAttr('Dude_Lt_Rye_UpLid_Mstr_Ctrl.translateY')
		Rt_EyeAim_CtrlFrown = cmds.getAttr('Dude_Rt_EyeAim_Ctrl.translateY')
		Lt_EyeAim_CtrlFrown =  cmds.getAttr('Dude_Lt_EyeAim_Ctrl.translateY')
		RightSideOfMouthTYFrown = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		RightSideOfMouthTZFrown =  cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateZ')
		LeftSideOfMouthTYFrown =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTZFrown= cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateZ')
		defaultFaceAttributes()
		
		
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=0 )#5ALEHA 0 
		
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0, ) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0, )
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=0 ,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=0 ,v=0)#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=0 )		
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 )	
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=0 )	
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0	
			
	
		
		#rearrange
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=20 ,v=0 )#5ALEHA 0 
		
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=LeftSideOfMouthTYFrown)
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20 ,v=LeftSideOfMouthTZFrown) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20,v=RightSideOfMouthTYFrown )
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20 ,v=RightSideOfMouthTZFrown)  
		
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=20,v=0 )#5ALEHA 0
		
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=LtBrowTyFrown )
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=20,v=RtBrowTyFrown )
		
		
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=Lt_Rye_UpLidFrown)
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20 ,v=Rt_Rye_UpLidFrown)
		
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=20 ,v=Lt_EyeAim_CtrlFrown)
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=20 ,v=Rt_EyeAim_CtrlFrown)
		
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0

		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		global  neckXFrown ,neckYFrown ,neckZFrown ,LtBrowTyFrown, RtBrowTyFrown, Rt_Rye_UpLidFrown, Lt_Rye_UpLidFrown, Rt_EyeAim_CtrlFrown, Lt_EyeAim_CtrlFrown, RightSideOfMouthTYFrown,RightSideOfMouthTZFrown,LeftSideOfMouthTYFrown,LeftSideOfMouthTZFrown
		neckXFrown= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckYFrown= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZFrown= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')
		
		
		LtBrowTyFrown = cmds.getAttr('Dude_Lt_Brow_3_Ctrl.translateY')
		RtBrowTyFrown =  cmds.getAttr('Dude_Rt_Brow_3_Ctrl.translateY')
		Rt_Rye_UpLidFrown = cmds.getAttr('Dude_Rt_Rye_UpLid_Mstr_Ctrl.translateY')
		Lt_Rye_UpLidFrown =  cmds.getAttr('Dude_Lt_Rye_UpLid_Mstr_Ctrl.translateY')
		Rt_EyeAim_CtrlFrown = cmds.getAttr('Dude_Rt_EyeAim_Ctrl.translateY')
		Lt_EyeAim_CtrlFrown =  cmds.getAttr('Dude_Lt_EyeAim_Ctrl.translateY')
		RightSideOfMouthTYFrown = cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateY')
		RightSideOfMouthTZFrown =  cmds.getAttr('Dude_Rt_Mouth_Crnr_Ctrl.translateZ')
		LeftSideOfMouthTYFrown =  cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateY')
		LeftSideOfMouthTZFrown= cmds.getAttr('Dude_Lt_Mouth_Crnr_Ctrl.translateZ')
		sliderFrownValue=cmds.intSliderGrp( sliderFrown,q=True,value=True)
		for x in range(sliderFrownValue+1):
			lastIndex=len(expressions)-1
			cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )	
			cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )
			
			
			
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=neckXFrown)
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=neckYFrown) #5ALEHA 0
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=neckZFrown )#5ALEHA 0 
			cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )#5ALEHA 0 
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20  ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=LeftSideOfMouthTYFrown)
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20 ,v=LeftSideOfMouthTZFrown) 
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=RightSideOfMouthTYFrown )
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1)*20 ,v=RightSideOfMouthTZFrown)  
			cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 )#5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=LtBrowTyFrown )
			cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=RtBrowTyFrown )
			cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=Lt_Rye_UpLidFrown)
			cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20,v=Rt_Rye_UpLidFrown)
			cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=Lt_EyeAim_CtrlFrown)
			cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=Rt_EyeAim_CtrlFrown)
			cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20 ,v=0 ) #5ALEHA 0
			expressions.append("frown")
	cmds.button(label='Animate', command=animateFrown,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))	
	cmds.showWindow(window)


def Surprise(*args):
	surpriseAttributes()
	window = cmds.window()
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='Neck Control', align='center',backgroundColor=(0.1,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='Neck Forwards/Backwards direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateX'  )
	cmds.attrFieldSliderGrp(label='Neck Right/Left direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateY'  )
	cmds.attrFieldSliderGrp(label='Neck Side/Side direction', minValue=-40, maxValue=40, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Neck_Ctrl.rotateZ'  )

	cmds.text( label='Eyebrow', align='center',backgroundColor=(0.0,0.0,0.1) ,height= 18)
	cmds.attrFieldSliderGrp(label='RtBrowTy(MiddleMuscle)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Brow_3_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LtBrowTy(MiddleMuscle)', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Brow_3_Ctrl.ty'  )
	cmds.text( label='EyeLid', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='RtTopEyeLid', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Rt_Rye_UpLid_Mstr_Ctrl.ty'  )
	cmds.attrFieldSliderGrp(label='LtTopEyeLid', minValue=-3.5, maxValue=3.8, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Lt_Rye_UpLid_Mstr_Ctrl.ty'  )
		
	cmds.text( label='Jaw', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	cmds.attrFieldSliderGrp(label='BottomJawTy', minValue=-5.681, maxValue=0, fieldMinValue=-100.0, fieldMaxValue=100.0 ,at='Dude_Jaw_Ctrl.ty'  )
		
	cmds.text( label='How many seconds do you want this expression to stay in the queue?', align='center',backgroundColor=(0.0,0.0,0.1),height= 18 )
	global sliderSurprise
	sliderSurprise=cmds.intSliderGrp( l="Time to spend",min=1,max=10, step = 1, field=True)

	def animateSurprise(*args):
		global LtBrowTySurprise,RtBrowTySurprise,Rt_Rye_UpLidSurprise,Lt_Rye_UpLidSurprise,JawControlTySurprise
		LtBrowTySurprise = cmds.getAttr('Dude_Lt_Brow_3_Ctrl.translateY')
		RtBrowTySurprise =  cmds.getAttr('Dude_Rt_Brow_3_Ctrl.translateY')
		Rt_Rye_UpLidSurprise = cmds.getAttr('Dude_Rt_Rye_UpLid_Mstr_Ctrl.translateY')
		Lt_Rye_UpLidSurprise =  cmds.getAttr('Dude_Lt_Rye_UpLid_Mstr_Ctrl.translateY')
		JawControlTySurprise= cmds.getAttr('Dude_Jaw_Ctrl.translateY')
		defaultFaceAttributes()
		
		
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=0  )#5ALEHA 0 
		
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
		cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=20 ,v=0)
		cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=20 ,v=0 )#5ALEHA 0 
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20 ,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 ) 
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=20,v=0 ) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=20 ,v=0)
		cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=20,v=0 )  
		cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=20 ,v=0) #5ALEHA 0
		cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=20 ,v=0)#5ALEHA 0
		cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=20 ,v=LtBrowTySurprise)
		cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=20  ,v=RtBrowTySurprise)
		cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20  ,v=Lt_Rye_UpLidSurprise)
		cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=20  ,v=Rt_Rye_UpLidSurprise)
		cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=20,v=0 )
		cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=20  ,v=JawControlTySurprise) #5ALEHA 0
		for x in range(21):
			cmds.currentTime( x, edit=True )
	def addExpression(*args):
		global	neckXSurprise ,neckYSurprise ,neckZSurprise, LtBrowTySurprise,RtBrowTySurprise,Rt_Rye_UpLidSurprise,Lt_Rye_UpLidSurprise,JawControlTySurprise
		neckXSurprise= cmds.getAttr('Dude_Neck_Ctrl.rotateX')
		neckYSurprise= cmds.getAttr('Dude_Neck_Ctrl.rotateY')
		neckZSurprise= cmds.getAttr('Dude_Neck_Ctrl.rotateZ')
		
		LtBrowTySurprise = cmds.getAttr('Dude_Lt_Brow_3_Ctrl.translateY')
		RtBrowTySurprise =  cmds.getAttr('Dude_Rt_Brow_3_Ctrl.translateY')
		Rt_Rye_UpLidSurprise = cmds.getAttr('Dude_Rt_Rye_UpLid_Mstr_Ctrl.translateY')
		Lt_Rye_UpLidSurprise =  cmds.getAttr('Dude_Lt_Rye_UpLid_Mstr_Ctrl.translateY')
		JawControlTySurprise= cmds.getAttr('Dude_Jaw_Ctrl.translateY')

		sliderSurpriseValue=cmds.intSliderGrp( sliderSurprise,q=True,value=True)
		for x in range(sliderSurpriseValue+1):
			lastIndex=len(expressions)-1
			cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )	
			cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=(lastIndex+1)*20  ,v=0 )
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=(lastIndex+1)*20  ,v=neckXSurprise)
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=(lastIndex+1)*20 ,v=neckYSurprise) #5ALEHA 0
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=(lastIndex+1)*20 ,v=neckZSurprise  )#5ALEHA 0 
			cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0)
			cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0 )#5ALEHA 0 
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 ) 
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(lastIndex+1) *20,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(lastIndex+1) *20,v=0 )  
			cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=0)#5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=LtBrowTySurprise)
			cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20  ,v=RtBrowTySurprise)
			cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20  ,v=Lt_Rye_UpLidSurprise)
			cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20  ,v=Rt_Rye_UpLidSurprise)
			cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20,v=0 )
			cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=(lastIndex+1) *20 ,v=JawControlTySurprise) #5ALEHA 0
			expressions.append("surprise")
		
	cmds.button(label='Animate', command=animateSurprise,backgroundColor=(0.0,0.0,0.1))
	cmds.button(label='Add to expression Queue', command=addExpression,backgroundColor=(0.0,0.0,0.1))

	cmds.showWindow(window)

	











def Execute(*args):
	cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=0  ,v=0)
	cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=0 ,v=0  )#5ALEHA 0 
	
	cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=0  ,v=0)
	cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=0  ,v=0 )	
	cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=0,v=0 )
	
	cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=0 ,v=0)
	cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
	cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=0 ,v=0 )#5ALEHA 0 
	cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0)
	cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 ) 
	cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=0 ,v=0)
	cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=0,v=0 )  
	cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=0 ,v=0) #5ALEHA 0
	cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=0,v=0 )#5ALEHA 0
	cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=0,v=0 )
	cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=0 ,v=0)
	cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0 ,v=0)
	cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=0,v=0)
	cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=0,v=0 )
	cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=0,v=0 )
	cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=0,v=0 ) #5ALEHA 0
	for i, x in enumerate(expressions):
		if x == "talk":
			cmds.setKeyframe('Dude_Lt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(i+1)*20  ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_LoLid_Mstr_Ctrl' ,attribute='translateY',time=(i+1)*20  ,v=0 )	
			cmds.setKeyframe('Dude_Lo_Mouth_Main_Ctrl' ,attribute='translateY',time=(i+1)*20  ,v=0 )
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateX',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateY',time=(i+1) *20,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Neck_Ctrl' ,attribute='rotateZ',time=(i+1) *20,v=0  )#5ALEHA 0 
			cmds.setKeyframe('Dude_MainEyeAim_Ctrl' ,attribute='translateX',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Lt_Brow_1_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 ) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_1_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0 )#5ALEHA 0 
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(i+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Lt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(i+1) *20,v=0 ) 
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateX',time=(i+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Rt_Mouth_Crnr_Ctrl' ,attribute='translateZ',time=(i+1) *20,v=0 )  
			cmds.setKeyframe('Dude_Lt_Brow_2_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0) #5ALEHA 0
			cmds.setKeyframe('Dude_Rt_Brow_2_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )#5ALEHA 0
			cmds.setKeyframe('Dude_Lt_Brow_3_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Rt_Brow_3_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Lt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Rt_Rye_UpLid_Mstr_Ctrl' ,attribute='translateY',time=(i+1) *20 ,v=0)
			cmds.setKeyframe('Dude_Lt_EyeAim_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Rt_EyeAim_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 )
			cmds.setKeyframe('Dude_Jaw_Ctrl' ,attribute='translateY',time=(i+1) *20,v=0 ) #5ALEHA 0
			
			
			
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
	#for x in range(len(expressions)* 21):
		#cmds.currentTime( x, edit=True )

		
def startAnimation(*args):
	cmds.currentTime(0)
	cmds.play( forward=True,sound="convo2" )
	
def ResetExpressionQueue(*args):
	global expressions
	expressions=[]
	cmds.cutKey('Dude_Rt_Rye_LoLid_Mstr_Ctrl','Dude_Lt_Rye_LoLid_Mstr_Ctrl','Dude_Lo_Mouth_Main_Ctrl','Dude_Neck_Ctrl','Dude_Rt_Brow_1_Ctrl' ,'Dude_Lt_Brow_1_Ctrl','Dude_MainEyeAim_Ctrl' ,'Dude_Lt_Mouth_Crnr_Ctrl' ,'Dude_Lt_Mouth_Crnr_Ctrl' ,'Dude_Lt_Mouth_Crnr_Ctrl' ,'Dude_Rt_Mouth_Crnr_Ctrl' ,'Dude_Rt_Mouth_Crnr_Ctrl' ,'Dude_Rt_Mouth_Crnr_Ctrl' ,'Dude_Lt_Brow_2_Ctrl' ,'Dude_Rt_Brow_2_Ctrl' ,'Dude_Lt_Brow_3_Ctrl' ,'Dude_Rt_Brow_3_Ctrl' ,'Dude_Lt_Rye_UpLid_Mstr_Ctrl' , 'Dude_Jaw_Ctrl','Dude_Rt_EyeAim_Ctrl','Dude_Lt_EyeAim_Ctrl' ,'Dude_Rt_Rye_UpLid_Mstr_Ctrl' , cl=True, time=(0,10000))
	#mel.eval("cutKey -time ":" -hierarchy none -controlPoints 0 -shape 1 {"Dude_Head_Ctrl", "Dude_Mid_Ctrl", "Dude_Nose__Mid_Ctrl", "Dude_Upteeth_Mid_Ctrl", "Dude_Nose_Lt_Ctrl1", "Dude_Nose_Rt_Ctrl", "Dude_Upteeth_Lt_Ctrl", "Dude_Upteeth_Rt_Ctrl", "Dude_Upteeth_Mstr_Ctrl", "Dude_Lt_Orbit_Master_Ctrl", "Dude_Rt_Orbit_Master_Ctrl", "Dude_Lt_EyeAim_Ctrl", "Dude_Rt_EyeAim_Ctrl", "Dude_FaceBot_Ctrl", "Dude_Lt_Eye_Attr_Ctrl", "Dude_Rt_Eye_Attr_Ctrl", "Dude_Lt_Eye_Master_Ctrl", "Dude_Rt_Eye_Master_Ctrl", "Dude_HairTaft_FK_Ctrl_5", "Dude_MainEyeAim_Ctrl", "Dude_FaceTop_Ctrl", "Dude_HairTaft_FK_Ctrl_1", "Dude_HairTaft_FK_Ctrl_2", "Dude_HairTaft_FK_Ctrl_3", "Dude_HairTaft_FK_Ctrl_4", "Dude_Taft_Master_Ctrl", "Dude_CheekTop_Lt_Ctrl1", "Dude_CheekTop_Rt_Ctrl", "ForeHead_Lt_B_1_Offset_Ctrl", "ForeHead_Mid_Offset_Ctrl", "ForeHead_Rt_A_Offset_Ctrl", "ForeHead_Rt_B_Offset_Ctrl", "ForeHead_Lt_A_1_Offset_Ctrl", "Dude_Lt_Brow_5_Ctrl", "Dude_Lt_Brow_4_Ctrl", "Dude_Lt_Brow_Mstr_Ctrl", "Dude_Rt_Brow_Mstr_Ctrl", "Dude_Lt_Brow_6_Ctrl", "Dude_Lt_Brow_3_Ctrl", "Dude_Lt_Brow_2_Ctrl", "Dude_Lt_Brow_1_Ctrl", "Dude_Rt_Brow_6_Ctrl", "Dude_Rt_Brow_5_Ctrl", "Dude_Rt_Brow_4_Ctrl", "Dude_Rt_Brow_3_Ctrl", "Dude_Rt_Brow_2_Ctrl", "Dude_Rt_Brow_1_Ctrl", "Dude_Mid_Brow_Ctrl", "Dude_Lt_Spot_Ctrl", "Dude_Lt_Rye_LoLid_Mstr_Ctrl", "Dude_Lt_Rye_UpLid_Mstr_Ctrl", "Dude_Rt_Spot_Ctrl", "Dude_Rt_Rye_LoLid_Mstr_Ctrl", "Dude_Rt_Rye_UpLid_Mstr_Ctrl", "Dude_Cheek_Lt_Ctrl1", "Dude_Cheek_Rt_Ctrl", "Dude_LoFace_Mstr_Ctrl", "Dude_Mouth_Master_Ctrl", "Dude_Jaw_Ctrl", "Dude_Lo_Mouth_Main_Ctrl", "Dude_Rt_LoLip_6_Ctrl", "Dude_Lo_Mouth_Rot_Ctrl", "Dude_Top_Mouth_Rot_Ctrl", "Dude_Top_Mouth_Main_Ctrl", "Dude_Rt_UpLip_0_Ctrl", "Dude_Lt_LoLip_2_Ctrl", "Dude_Rt_LoLip_2_Ctrl", "Dude_Lt_LoLip_4_Ctrl", "Dude_Rt_LoLip_4_Ctrl", "Dude_Lt_Mouth_Crnr_Ctrl", "Dude_Lt_UpLip_6_Ctrl", "Dude_Rt_Mouth_Crnr_Ctrl", "Dude_Rt_UpLip_6_Ctrl", "Dude_Lt_UpLip_4_Ctrl", "Dude_Rt_UpLip_4_Ctrl", "Dude_Rt_UpLip_2_Ctrl", "Dude_Lt_UpLip_2_Ctrl", "Dude_x_tongue_Extend_ctrl_ctl", "Dude_Tongue_Master_Ctrl", "Dude_Loteeth_Mid_Ctrl", "Dude_Loteeth_Lt_Ctrl", "Dude_Loteeth_Rt_Ctrl", "Dude_Loteeth_Mstr_Ctrl", "Dude_x_tongue_9_ctrl_ctl", "Dude_x_tongue_8_ctrl_ctl", "Dude_x_tongue_7_ctrl_ctl", "Dude_x_tongue_6_ctrl_ctl", "Dude_x_tongue_5_ctrl_ctl", "Dude_x_tongue_4_ctrl_ctl", "Dude_x_tongue_3_ctrl_ctl", "Dude_x_tongue_2_ctrl_ctl", "Dude_x_tongue_1_ctrl_ctl", "JasmineRose_Rig_V_1:JasmineRose_Eyes_Lt_Aim_Ctrl", "JasmineRose_Rig_V_1:JasmineRose_Eyes_Rt_Aim_Ctrl", "JasmineRose_Rig_V_1:JasmineRose_Eyes_Aim_Master_Ctrl", "Cornea_Lt_geo", "Dude_Rt_Spot_Geo", "Eye_Rt_geo", "UpperTeeth_geo", "Dude_Lt_Spot_Geo", "Tongue_geo", "Cornea_Rt_geo", "EyeLash_geo", "Eye_Lt_geo", "LowTeeth_geo", "Hair_geo", "Brows_geo", "Body_geo"};")
def resetFace(*args):
	defaultFaceAttributes()
	



#msh beysave el values ama adoos add facial expression i guess? fa adeef el global variable declaration bardo fee add expression?
# run el code b animate el awel then save exp





cmds.window(width=300,t="Dude Facial Expressions")
cmds.columnLayout(adjustableColumn=True)
cmds.button(label='Smile', command=Smile,backgroundColor=(0.0,0.0,0.1))
cmds.button(label='Frown', command=Frown,backgroundColor=(0.0,0.3,0.1))
cmds.button(label='Shock', command=Surprise, backgroundColor=(0.0,0.0,0.5))
cmds.button(label='Happy', command=Happy, backgroundColor=(0.0,0.5,0.5))
cmds.button(label='Angry', command=Angry,backgroundColor=(0.5,0.0,0.1))

##cmds.button(label='Paranoia', command=Paranoia, backgroundColor=(0.5,0.5,1))
cmds.button(label='Idle', command=Talk, backgroundColor=(0.5,0.5,1))

#cmds.button(label='Disgust', command=Disgust, backgroundColor=(0.5,0.5,0))
cmds.button(label='Add all keyframes', command=Execute, backgroundColor=(0.5,0.5,0.5))
cmds.button(label='Reset facial expressions', command=ResetExpressionQueue, backgroundColor=(1,0.5,0.5))
cmds.button(label='Start Animation', command=startAnimation, backgroundColor=(0.5,1,0.5))

cmds.button(label='Default Face', command=resetFace)


cmds.showWindow()