#!/usr/bin/env python3
"""
Competitor Analysis Utility
Handles competitor tracking and strategic analysis.
"""

import json
import os
import random
from datetime import datetime
from typing import Dict, List, Any, Optional

class CompetitorAnalysis:
    """Handles competitor tracking and analysis."""
    
    def __init__(self):
        self.competitors_file = "data/competitors.json"
        self.ensure_data_file()
    
    def ensure_data_file(self):
        """Ensure the competitors data file exists."""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.competitors_file):
            with open(self.competitors_file, 'w') as f:
                json.dump([], f)
    
    async def add_competitor(self, name: str, platforms: Dict[str, str]) -> Dict[str, Any]:
        """Add a new competitor to track."""
        try:
            competitors = self._load_competitors()
            
            # Check if competitor already exists
            if any(comp["name"].lower() == name.lower() for comp in competitors):
                return {"error": f"Competitor '{name}' already exists"}
            
            competitor = {
                "name": name,
                "platforms": platforms,
                "added_on": datetime.now().isoformat(),
                "last_analyzed": None,
                "metrics": {}
            }
            
            competitors.append(competitor)
            self._save_competitors(competitors)
            
            return {"message": f"Competitor '{name}' added successfully"}
            
        except Exception as e:
            return {"error": f"Failed to add competitor: {str(e)}"}
    
    async def remove_competitor(self, name: str) -> Dict[str, Any]:
        """Remove a competitor from tracking."""
        try:
            competitors = self._load_competitors()
            original_count = len(competitors)
            
            competitors = [comp for comp in competitors if comp["name"].lower() != name.lower()]
            
            if len(competitors) < original_count:
                self._save_competitors(competitors)
                return {"message": f"Competitor '{name}' removed successfully"}
            else:
                return {"error": f"Competitor '{name}' not found"}
                
        except Exception as e:
            return {"error": f"Failed to remove competitor: {str(e)}"}
    
    async def list_competitors(self) -> Dict[str, Any]:
        """List all tracked competitors."""
        try:
            competitors = self._load_competitors()
            
            return {
                "competitors": competitors,
                "total": len(competitors),
                "last_updated": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"Failed to list competitors: {str(e)}"}
    
    async def analyze_competitor_strategy(self, name: str) -> Dict[str, Any]:
        """Analyze a specific competitor's strategy."""
        try:
            competitors = self._load_competitors()
            competitor = next((comp for comp in competitors if comp["name"].lower() == name.lower()), None)
            
            if not competitor:
                return {"error": f"Competitor '{name}' not found"}
            
            # Generate mock analysis data
            analysis = self._generate_competitor_analysis(competitor)
            
            # Update last analyzed timestamp
            competitor["last_analyzed"] = datetime.now().isoformat()
            competitor["metrics"] = analysis["metrics"]
            self._save_competitors(competitors)
            
            return {
                "competitor": name,
                "platforms": competitor["platforms"],
                "analysis": analysis,
                "analyzed_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"Failed to analyze competitor: {str(e)}"}
    
    async def compare_competitors(self, competitor_names: List[str]) -> Dict[str, Any]:
        """Compare multiple competitors."""
        try:
            competitors = self._load_competitors()
            found_competitors = []
            
            for name in competitor_names:
                competitor = next((comp for comp in competitors if comp["name"].lower() == name.lower()), None)
                if competitor:
                    found_competitors.append(competitor)
            
            if len(found_competitors) < 2:
                return {"error": "At least 2 competitors required for comparison"}
            
            comparison = self._generate_comparison(found_competitors)
            
            return {
                "comparison": comparison,
                "competitors_compared": [comp["name"] for comp in found_competitors],
                "compared_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"Failed to compare competitors: {str(e)}"}
    
    def _load_competitors(self) -> List[Dict[str, Any]]:
        """Load competitors from file."""
        try:
            with open(self.competitors_file, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def _save_competitors(self, competitors: List[Dict[str, Any]]) -> None:
        """Save competitors to file."""
        with open(self.competitors_file, 'w') as f:
            json.dump(competitors, f, indent=2)
    
    def _generate_competitor_analysis(self, competitor: Dict[str, Any]) -> Dict[str, Any]:
        """Generate mock competitor analysis."""
        platforms = list(competitor["platforms"].keys())
        
        # Generate mock metrics
        metrics = {}
        for platform in platforms:
            metrics[platform] = {
                "followers": random.randint(500, 10000),
                "engagement_rate": round(random.uniform(1.0, 6.0), 2),
                "posts_per_week": random.randint(3, 15),
                "avg_likes": random.randint(50, 500),
                "avg_comments": random.randint(5, 50)
            }
        
        # Analyze content strategy
        content_strategy = {
            "post_types": {
                "images": random.randint(40, 70),
                "videos": random.randint(15, 35),
                "carousels": random.randint(5, 20),
                "text": random.randint(0, 15)
            },
            "top_topics": {
                "product_showcase": random.randint(20, 40),
                "behind_scenes": random.randint(10, 25),
                "user_generated": random.randint(5, 20),
                "educational": random.randint(10, 30),
                "promotional": random.randint(5, 25)
            }
        }
        
        # Normalize percentages
        for category in content_strategy.values():
            total = sum(category.values())
            for key in category:
                category[key] = round(category[key] * 100 / total, 1)
        
        # Generate insights
        insights = self._generate_competitor_insights(metrics, content_strategy)
        
        return {
            "metrics": metrics,
            "content_strategy": content_strategy,
            "posting_schedule": {
                "most_active_days": random.sample(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 3),
                "peak_hours": random.sample(["9AM", "12PM", "3PM", "6PM", "9PM"], 2)
            },
            "ai_insights": insights
        }
    
    def _generate_competitor_insights(self, metrics: Dict, content_strategy: Dict) -> str:
        """Generate AI insights about competitor."""
        insights = []
        
        # Analyze engagement rates
        avg_engagement = sum(platform["engagement_rate"] for platform in metrics.values()) / len(metrics)
        if avg_engagement > 4:
            insights.append("Strong engagement across platforms")
        elif avg_engagement > 2:
            insights.append("Moderate engagement with room for improvement")
        else:
            insights.append("Low engagement suggests content optimization needed")
        
        # Analyze content mix
        post_types = content_strategy.get("post_types", {})
        if post_types.get("videos", 0) > 30:
            insights.append("Heavy focus on video content")
        if post_types.get("images", 0) > 60:
            insights.append("Image-heavy content strategy")
        
        # Analyze topics
        topics = content_strategy.get("top_topics", {})
        top_topic = max(topics.items(), key=lambda x: x[1]) if topics else None
        if top_topic:
            insights.append(f"Primary focus on {top_topic[0].replace('_', ' ')} content")
        
        return " • ".join(insights) if insights else "Balanced content strategy with steady engagement."
    
    def _generate_comparison(self, competitors: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comparison data between competitors."""
        comparison = {
            "followers": {},
            "engagement": {},
            "posting_frequency": {}
        }
        
        for competitor in competitors:
            name = competitor["name"]
            
            # Mock comparison data
            comparison["followers"][name] = random.randint(1000, 15000)
            comparison["engagement"][name] = round(random.uniform(1.5, 5.5), 2)
            comparison["posting_frequency"][name] = round(random.uniform(3, 12), 1)
        
        return comparison

# Global instance
competitor_analysis = CompetitorAnalysis()
