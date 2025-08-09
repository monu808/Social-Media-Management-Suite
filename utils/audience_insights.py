#!/usr/bin/env python3
"""
Audience Insights Utility
Provides detailed audience analytics and insights.
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

class AudienceInsights:
    """Handles audience analytics and insights generation."""
    
    def __init__(self):
        self.mock_enabled = True  # Using mock data for demo
    
    async def get_audience_demographics(self, platform: str) -> Dict[str, Any]:
        """Get demographic breakdown of the audience."""
        try:
            demographics = self._generate_mock_demographics(platform)
            
            return {
                "platform": platform,
                "demographics": demographics,
                "last_updated": datetime.now().isoformat(),
                "total_audience": demographics.get("total_followers", 0)
            }
            
        except Exception as e:
            return {"error": f"Failed to get demographics: {str(e)}"}
    
    async def get_follower_growth(self, platform: str, days: int = 30) -> Dict[str, Any]:
        """Get follower growth analytics."""
        try:
            current_followers = random.randint(800, 3000)
            growth_rate = random.uniform(1.5, 8.0)
            total_growth = int(current_followers * growth_rate / 100)
            
            return {
                "platform": platform,
                "period_days": days,
                "follower_count": current_followers,
                "follower_growth": {
                    "total": total_growth,
                    "percentage": round(growth_rate, 1),
                    "average_daily": round(total_growth / days, 1)
                },
                "last_updated": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"Failed to get follower growth: {str(e)}"}
    
    async def get_engagement_metrics(self, platform: str, days: int = 7) -> Dict[str, Any]:
        """Get detailed engagement metrics."""
        try:
            metrics = self._generate_mock_engagement(platform)
            
            return {
                "platform": platform,
                "period_days": days,
                "total_posts": random.randint(10, 50),
                "average_metrics": metrics,
                "top_performing_posts": self._generate_top_posts(),
                "last_updated": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"Failed to get engagement metrics: {str(e)}"}
    
    async def generate_audience_report(self, platform: str) -> Dict[str, Any]:
        """Generate comprehensive audience report."""
        try:
            demographics = await self.get_audience_demographics(platform)
            growth = await self.get_follower_growth(platform)
            engagement = await self.get_engagement_metrics(platform)
            
            # Generate AI insights
            insights = self._generate_audience_insights(demographics, growth, engagement)
            
            return {
                "platform": platform,
                "demographics": demographics,
                "follower_growth": growth,
                "engagement_metrics": engagement,
                "insights": insights,
                "generated_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"Failed to generate audience report: {str(e)}"}
    
    def _generate_mock_demographics(self, platform: str) -> Dict[str, Any]:
        """Generate realistic mock demographic data."""
        age_groups = {
            "18-24": random.randint(15, 35),
            "25-34": random.randint(25, 45),
            "35-44": random.randint(15, 30),
            "45-54": random.randint(5, 20),
            "55+": random.randint(2, 15)
        }
        
        # Normalize to 100%
        total = sum(age_groups.values())
        age_groups = {k: round(v * 100 / total, 1) for k, v in age_groups.items()}
        
        gender_split = {
            "Female": random.randint(45, 65),
            "Male": 0,
            "Other": random.randint(1, 5)
        }
        gender_split["Male"] = 100 - gender_split["Female"] - gender_split["Other"]
        
        locations = {
            "United States": random.randint(25, 40),
            "India": random.randint(15, 30),
            "United Kingdom": random.randint(8, 15),
            "Canada": random.randint(5, 12),
            "Australia": random.randint(3, 8),
            "Others": 0
        }
        total_loc = sum(locations.values())
        locations["Others"] = 100 - total_loc
        
        return {
            "age_groups": age_groups,
            "gender": gender_split,
            "locations": locations,
            "total_followers": random.randint(800, 5000)
        }
    
    def _generate_mock_engagement(self, platform: str) -> Dict[str, Any]:
        """Generate mock engagement metrics."""
        base_engagement = {
            "instagram": {"likes": 150, "comments": 25, "shares": 8, "saves": 12},
            "twitter": {"likes": 45, "retweets": 12, "replies": 8, "quotes": 3},
            "facebook": {"likes": 80, "comments": 15, "shares": 6, "reactions": 20},
            "linkedin": {"likes": 35, "comments": 12, "shares": 5, "reactions": 8}
        }
        
        metrics = base_engagement.get(platform, base_engagement["instagram"]).copy()
        
        # Add some randomness
        for key in metrics:
            variation = random.uniform(0.7, 1.4)
            metrics[key] = int(metrics[key] * variation)
        
        # Calculate engagement rate
        total_engagement = sum(metrics.values())
        avg_reach = random.randint(1000, 5000)
        engagement_rate = round((total_engagement / avg_reach) * 100, 2)
        
        metrics["engagement_rate"] = engagement_rate
        metrics["average_reach"] = avg_reach
        
        return metrics
    
    def _generate_top_posts(self) -> List[Dict[str, Any]]:
        """Generate mock top performing posts."""
        posts = []
        for i in range(5):
            engagement_rate = random.uniform(2.5, 8.0)
            posts.append({
                "post_id": f"post_{i+1}",
                "content_type": random.choice(["image", "video", "carousel", "text"]),
                "metrics": {
                    "engagement_rate": round(engagement_rate, 2),
                    "reach": random.randint(500, 3000),
                    "impressions": random.randint(800, 5000)
                }
            })
        
        return sorted(posts, key=lambda x: x["metrics"]["engagement_rate"], reverse=True)
    
    def _generate_audience_insights(self, demographics: Dict, growth: Dict, engagement: Dict) -> str:
        """Generate AI-powered insights based on data."""
        insights = []
        
        # Demographics insights
        if demographics.get("demographics"):
            age_data = demographics["demographics"].get("age_groups", {})
            dominant_age = max(age_data.items(), key=lambda x: x[1]) if age_data else None
            if dominant_age:
                insights.append(f"Your primary audience is {dominant_age[0]} age group ({dominant_age[1]}%)")
        
        # Growth insights
        if growth.get("follower_growth"):
            growth_rate = growth["follower_growth"].get("percentage", 0)
            if growth_rate > 5:
                insights.append("Excellent follower growth rate indicates strong content resonance")
            elif growth_rate > 2:
                insights.append("Steady growth - consider increasing posting frequency")
            else:
                insights.append("Growth could be improved with more engaging content")
        
        # Engagement insights
        if engagement.get("average_metrics"):
            eng_rate = engagement["average_metrics"].get("engagement_rate", 0)
            if eng_rate > 4:
                insights.append("High engagement rate shows strong audience connection")
            elif eng_rate > 2:
                insights.append("Good engagement - focus on replicating top-performing content")
            else:
                insights.append("Consider optimizing posting times and content strategy")
        
        return " • ".join(insights) if insights else "Audience data suggests steady performance with room for optimization."

# Global instance
audience_insights = AudienceInsights()
