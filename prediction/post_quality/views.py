from django.shortcuts import render
from .mll_model import PostQualityPredictor


def predict_post_quality(request):
    prediction = None
    if request.method == 'POST':
        try:
            reputation = float(request.POST.get('reputation'))
            interaction = float(request.POST.get('delta'))
            print(reputation,  interaction)
            
            predictor = PostQualityPredictor()
            prediction = predictor.predict(reputation, interaction)
            return render(request, 'post_quality.html', {
                'user_reputation': reputation,
                'mpxr':interaction,
                'prediction': prediction
            })
        except (ValueError, TypeError):          
            prediction = "Invalid input"
        except (ValueError, TypeError) as e:
            prediction = "Invalid input"
            #print the error
            print(e)    

    
    return render(request, 'post_quality.html', {'prediction': prediction})