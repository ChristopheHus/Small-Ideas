#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXTURE_SHADER

varying vec4 vertTexCoord;
uniform sampler2D texture;
uniform int blurRad;
uniform vec2 texOffset;
uniform vec2 blurVec;
const float PI = 3.14159265;


/*
(cos(x*x*1.553635) * -5.767909 + sin(x*x*1.553635) * 46.164397) * exp(-4.338459* x*x)
(cos(x*x*4.693183) * 9.795391 + sin(x*x*4.693183) * -15.227561) * exp(-3.839993* x*x)
(cos(x*x*8.178137) * -3.048324 + sin(x*x*8.178137) * 0.302959) * exp(-2.791880* x*x)
(cos(x*x*12.328289) * 0.010001 + sin(x*x*12.328289) * 0.244650) * exp(-1.342190* x*x)
*/

void main()
{
	float sigma = sqrt(1./(2.*4.338459));
	float s2 = 1.553635;
	
	vec4 tmp;
	
	vec2 p = vertTexCoord.st;

	vec3 incrGauss;
	vec3 incrGaussRe;
	vec3 incrGaussIm;
	
	incrGauss.x = 1.0 / (sqrt(2.0 * PI) * sigma);
	incrGauss.y = exp(-0.5 / (sigma * sigma));
	incrGauss.z = incrGauss.y * incrGauss.y;
	
	incrGaussRe.x = 1.;
	incrGaussIm.x = 0.;
	incrGaussRe.y = cos(s2);
	incrGaussIm.y = sin(s2);
	incrGaussRe.z = incrGaussRe.y * incrGaussRe.y - incrGaussIm.y * incrGaussIm.y;
	incrGaussIm.z = 2. * incrGaussRe.y * incrGaussIm.y;


	vec4 avgValue = vec4(0.0, 0.0, 0.0, 0.0);
	float coefficientSum = 0.0;

	avgValue += texture2D(texture, p) * (incrGaussRe.x);//(-5.767909*incrGaussRe.x + 46.164397*incrGaussIm.x);
	coefficientSum += incrGauss.x;
	incrGauss.xy *= incrGauss.yz;
	
	tmp = vec4(incrGaussRe.xy, incrGauss.xy);
	incrGaussRe.x = tmp.x * tmp.z - tmp.y * tmp.w;
	incrGaussIm.x = tmp.x * tmp.w + tmp.y * tmp.z;
	incrGaussRe.y = tmp.z * incrGaussRe.z - tmp.w * incrGaussIm.z;
	incrGaussIm.y = tmp.z * incrGaussIm.z + tmp.w * incrGaussRe.z;
	
	for (float i = 1.0; i <= blurRad; i++)
	{
		avgValue += texture2D(texture, p - i * texOffset * blurVec) * (incrGaussRe.x);       
		avgValue += texture2D(texture, p + i * texOffset * blurVec) * (incrGaussRe.x);        
		coefficientSum += 2.0 * incrGauss.x;
		
		incrGauss.xy *= incrGauss.yz;
		tmp = vec4(incrGaussRe.xy, incrGauss.xy);
		incrGaussRe.x = tmp.x * tmp.z - tmp.y * tmp.w;
		incrGaussIm.x = tmp.x * tmp.w + tmp.y * tmp.z;
		incrGaussRe.y = tmp.z * incrGaussRe.z - tmp.w * incrGaussIm.z;
		incrGaussIm.y = tmp.z * incrGaussIm.z + tmp.w * incrGaussRe.z;
	}

	gl_FragColor = avgValue / coefficientSum;
}