#!/usr/bin/env python3
"""
Hashtag Engine Utility
Advanced hashtag generation and optimization.
"""

import re
import random
from typing import Dict, List, Any, Optional

class HashtagEngine:
    """Advanced hashtag generation engine."""
    
    def __init__(self):
        self.trending_hashtags = self._load_trending_hashtags()
        self.niche_hashtags = self._load_niche_hashtags()
    
    def _load_trending_hashtags(self) -> Dict[str, List[str]]:
        """Load trending hashtags by platform."""
        return {
            "instagram": [
                "#instagood", "#photooftheday", "#love", "#instadaily", "#picoftheday",
                "#instagram", "#followme", "#instamood", "#style", "#happy"
            ],
            "twitter": [
                "#trending", "#news", "#today", "#breaking", "#viral",
                "#discussion", "#opinion", "#tech", "#business", "#life"
            ],
            "linkedin": [
                "#leadership", "#innovation", "#business", "#career", "#professional",
                "#networking", "#growth", "#success", "#strategy", "#development"
            ]
        }
    
    def _load_niche_hashtags(self) -> Dict[str, Dict[str, List[str]]]:
        """Load niche hashtags by topic and platform."""
        return {
            "mythology": {
                "instagram": ["#mythology", "#ancientmyths", "#greekmythology", "#norsemythology", "#legends"],
                "twitter": ["#mythology", "#myths", "#ancientstories", "#folklore", "#legends"],
                "linkedin": ["#culturalheritage", "#storytelling", "#history", "#mythology", "#education"]
            },
            "technology": {
                "instagram": ["#tech", "#innovation", "#gadgets", "#AI", "#future"],
                "twitter": ["#tech", "#innovation", "#AI", "#coding", "#startup"],
                "linkedin": ["#technology", "#innovation", "#digitaltransformation", "#AI", "#tech"]
            },
            "business": {
                "instagram": ["#business", "#entrepreneur", "#startup", "#success", "#hustle"],
                "twitter": ["#business", "#entrepreneur", "#startup", "#growth", "#strategy"],
                "linkedin": ["#business", "#leadership", "#strategy", "#growth", "#innovation"]
            }
        }
    
    async def generate_hashtags(self, content: str, platform: str = "instagram", 
                              count: int = 10, strategy: str = "mixed") -> Dict[str, Any]:
        """Generate hashtags using advanced analysis."""
        try:
            # Extract keywords from content
            keywords = self._extract_keywords(content)
            
            # Determine topic/niche
            topic = self._identify_topic(content, keywords)
            
            # Generate hashtags based on strategy
            hashtags = []
            
            if strategy == "trending":
                hashtags = self._get_trending_hashtags(platform, count)
            elif strategy == "niche":
                hashtags = self._get_niche_hashtags(topic, platform, count)
            elif strategy == "branded":
                hashtags = self._get_branded_hashtags(keywords, count)
            else:  # mixed
                hashtags = self._get_mixed_hashtags(topic, platform, keywords, count)
            
            # Add difficulty/competition level
            hashtags_with_difficulty = []
            for hashtag in hashtags:
                difficulty = self._assess_hashtag_difficulty(hashtag)
                hashtags_with_difficulty.append({
                    "hashtag": hashtag,
                    "difficulty": difficulty
                })
            
            return {
                "hashtags": hashtags,
                "analysis": {
                    "keywords": keywords,
                    "topic": topic,
                    "sentiment": self._analyze_sentiment(content)
                },
                "recommendations": self._get_hashtag_recommendations(platform, strategy),
                "method": "advanced_engine"
            }
            
        except Exception as e:
            return {"error": f"Failed to generate hashtags: {str(e)}"}
    
    def _extract_keywords(self, content: str) -> List[str]:
        """Extract relevant keywords from content."""
        # Remove special characters and split
        words = re.findall(r'\b[a-zA-Z]{3,}\b', content.lower())
        
        # Filter out common stop words
        stop_words = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had',
            'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his',
            'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy',
            'did', 'she', 'use', 'way', 'will', 'with', 'this', 'that', 'they'
        }
        
        keywords = [word for word in words if word not in stop_words and len(word) > 3]
        return list(dict.fromkeys(keywords))[:10]  # Remove duplicates, limit to 10
    
    def _identify_topic(self, content: str, keywords: List[str]) -> str:
        """Identify the main topic/niche from content."""
        topic_keywords = {
            "mythology": ["myth", "god", "goddess", "legend", "ancient", "hero", "story", "folklore"],
            "technology": ["tech", "digital", "software", "app", "code", "data", "ai", "innovation"],
            "business": ["business", "entrepreneur", "startup", "success", "marketing", "growth"],
            "lifestyle": ["life", "health", "fitness", "food", "travel", "style", "home", "wellness"],
            "education": ["learn", "education", "study", "knowledge", "skill", "training", "course"]
        }
        
        content_lower = content.lower()
        for topic, topic_words in topic_keywords.items():
            if any(word in content_lower or word in keywords for word in topic_words):
                return topic
        
        return "general"
    
    def _get_trending_hashtags(self, platform: str, count: int) -> List[str]:
        """Get trending hashtags for the platform."""
        trending = self.trending_hashtags.get(platform, self.trending_hashtags["instagram"])
        return random.sample(trending, min(count, len(trending)))
    
    def _get_niche_hashtags(self, topic: str, platform: str, count: int) -> List[str]:
        """Get niche-specific hashtags."""
        niche_tags = self.niche_hashtags.get(topic, {}).get(platform, [])
        if not niche_tags:
            # Fallback to general niche hashtags
            niche_tags = [f"#{topic}", f"#{topic}community", f"#{topic}lovers", f"#{topic}tips"]
        
        return niche_tags[:count]
    
    def _get_branded_hashtags(self, keywords: List[str], count: int) -> List[str]:
        """Generate branded hashtags from keywords."""
        branded = []
        for keyword in keywords[:count]:
            branded.append(f"#{keyword}")
            if len(branded) >= count:
                break
        return branded
    
    def _get_mixed_hashtags(self, topic: str, platform: str, keywords: List[str], count: int) -> List[str]:
        """Get a mix of trending, niche, and keyword-based hashtags."""
        hashtags = []
        
        # 40% trending
        trending_count = max(1, count * 40 // 100)
        hashtags.extend(self._get_trending_hashtags(platform, trending_count))
        
        # 40% niche
        niche_count = max(1, count * 40 // 100)
        hashtags.extend(self._get_niche_hashtags(topic, platform, niche_count))
        
        # 20% keyword-based
        keyword_count = count - len(hashtags)
        hashtags.extend(self._get_branded_hashtags(keywords, keyword_count))
        
        return list(dict.fromkeys(hashtags))[:count]  # Remove duplicates
    
    def _assess_hashtag_difficulty(self, hashtag: str) -> str:
        """Assess the competition difficulty of a hashtag."""
        # Simple assessment based on hashtag characteristics
        if len(hashtag) > 20:
            return "low"
        elif len(hashtag) > 15:
            return "medium"
        else:
            return "high"
    
    def _analyze_sentiment(self, content: str) -> str:
        """Simple sentiment analysis."""
        positive_words = ["good", "great", "amazing", "awesome", "love", "best", "perfect", "excellent"]
        negative_words = ["bad", "terrible", "hate", "worst", "awful", "horrible", "disappointing"]
        
        content_lower = content.lower()
        positive_count = sum(1 for word in positive_words if word in content_lower)
        negative_count = sum(1 for word in negative_words if word in content_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
    def _get_hashtag_recommendations(self, platform: str, strategy: str) -> List[str]:
        """Get platform-specific hashtag recommendations."""
        recommendations = {
            "instagram": [
                "Use 20-30 hashtags for maximum reach",
                "Mix popular and niche hashtags",
                "Place hashtags in comments to keep captions clean"
            ],
            "twitter": [
                "Use 1-2 hashtags per tweet",
                "Focus on trending and relevant hashtags",
                "Keep hashtags short and memorable"
            ],
            "linkedin": [
                "Use 3-5 professional hashtags",
                "Focus on industry-relevant tags",
                "Avoid overly casual hashtags"
            ]
        }
        
        return recommendations.get(platform, recommendations["instagram"])

# Global instance
hashtag_engine = HashtagEngine()
